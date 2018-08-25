SCOPE = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

TABLE_NAME = 'СКЛАД'
WORKSHEET_NO = 0
HEAD_ROW = 2
COLUMNS = ['НАИМЕНОВАНИЕ', 'Артикул', 'Олег', 'Женя']
MAIN_COLUMNS = ['НАИМЕНОВАНИЕ', 'Артикул']

DELIMITER = '\t'

from .local import *
