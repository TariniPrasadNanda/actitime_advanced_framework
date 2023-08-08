""" all the excel file related functions """
import xlrd


def read_locators(file_path, sheet_name):
	work_book = xlrd.open_workbook(file_path)
	work_sheet = work_book.sheet_by_name(sheet_name)

	rows = work_sheet.get_rows()
	header = next(rows)

	data = {}
	for row in rows:
		data[row[0].value] = (row[1].value, row[2].value)

	return data

