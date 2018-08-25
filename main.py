import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv
import config


def clean_str(s):
    result = s.replace('\n', ' ')
    while '  ' in result:
        result = result.replace('  ', ' ')
    return result.strip(' ')


def get_worksheet():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        config.CREDENTIALS, config.SCOPE
    )
    client = gspread.authorize(credentials)
    return client.open(config.TABLE_NAME).get_worksheet(config.WORKSHEET_NO)


def get_rows(sheet):
    list_of_hashes = sheet.get_all_records(head=config.HEAD_ROW)
    for el in list_of_hashes:
        if not (all(el[k] for k in config.MAIN_COLUMNS)):
            continue
        for k in config.MAIN_COLUMNS:
            el[k] = clean_str(el[k])
        yield (el[k] for k in config.COLUMNS)


def write_csv(rows):
    with open(config.CSV_FILE, 'w') as bg_csv_file:
        bg_csv = csv.writer(bg_csv_file, delimiter=config.DELIMITER)
        for row in rows:
            bg_csv.writerow(row)


if __name__ == '__main__':
    try:
        worksheet = get_worksheet()
        write_csv(get_rows(worksheet))
    except Exception:
        config.raven_client.captureException()
