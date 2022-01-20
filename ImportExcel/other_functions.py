import xlrd
from django.utils import timezone


def calc_excel(file):
    status_unknown = 'status unknown'
    rb = xlrd.open_workbook(file.path)
    sheet = rb.sheet_by_index(0)
    column_names = sheet.row_values(0)
    if ('before' not in column_names) or ('after' not in column_names):
        return status_unknown, timezone.now()
    before_index = column_names.index('before')
    after_index = column_names.index('after')
    before_column = [int(i) for i in sheet.col_values(before_index)[1:] if i != '']
    after_column = [int(i) for i in sheet.col_values(after_index)[1:] if i != '']
    if len(before_column) < len(after_column):
        l1 = before_column
        l2 = after_column
        name = 'added'
    else:
        l1 = after_column
        l2 = before_column
        name = 'removed'
    for li in l1:
        try:
            l2.remove(li)
        except Exception as e:
            return status_unknown, timezone.now()
    if len(l2) == 1:
        return f'{name}: {l2[0]}', timezone.now()
    else:
        return status_unknown, timezone.now()
