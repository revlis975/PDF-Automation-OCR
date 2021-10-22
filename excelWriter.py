import xlsxwriter


class Excel():
    def __init__(self) -> None:
        pass

    def write(self, Extracted_data, inv, fr, to, name):

        # Workbook creation and adding worksheets
        workbook = xlsxwriter.Workbook(name)
        worksheet = workbook.add_worksheet()

        # Add a bold format to use to highlight cells.
        bold = workbook.add_format({'bold': True})

        # Adjust the column width.
        worksheet.set_column(1, 0, 40)
        worksheet.set_column(1, 1, 40)
        worksheet.set_column(1, 2, 40)
        worksheet.set_column(1, 3, 40)
        worksheet.set_column(1, 4, 40)

        # Writing data headers
        worksheet.write('A1', 'Invoice Number', bold)
        worksheet.write('B1', 'Senders Address', bold)
        worksheet.write('C1', 'Receivers Address', bold)
        worksheet.write('D1', 'Phone Number', bold)
        worksheet.write('E1', 'E-Mail', bold)

        # To start from the first cell
        row = 1
        col = 0

        worksheet.write(row, col, inv)
        col += 1
        worksheet.write(row, col, fr)
        col += 1
        worksheet.write(row, col, to)
        col += 1

        x = 0
        for i in Extracted_data:
            s = ''
            for j in Extracted_data[x]:
                s = s + j + ", "
            worksheet.write(row, col, s)
            col += 1
            x += 1

        workbook.close()
