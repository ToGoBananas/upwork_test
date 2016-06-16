import xlrd


def parse_excel(files=None, category_cell_name=None, money_cell_name=None):
    book = xlrd.open_workbook(file_contents=files['file'].read())
    sh = book.sheet_by_index(0)
    first_row_cells = [cell.value for cell in sh.row(0)]
    class_cell_index = first_row_cells.index(category_cell_name)
    money_cell_index = first_row_cells.index(money_cell_name)
    result = {}

    for row_index in range(1, sh.nrows):
        class_cell = sh.cell_value(rowx=row_index, colx=class_cell_index)
        try:
            money_cell = float(sh.cell_value(rowx=row_index, colx=money_cell_index))
        except ValueError:
            pass
        else:
            if not result.get(class_cell):
                result[class_cell] = money_cell
            else:
                result[class_cell] += money_cell

    return result