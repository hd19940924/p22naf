#coding:utf-8
import xlrd
from xlutils.copy import copy
import getpathInfo
import os
path = getpathInfo.get_Path()
class OperationExcel:
	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id	
		else:
			xlsPath = os.path.join(path, "dataconfig" ,"case1.xls")
			self.file_name = xlsPath#'../dataconfig/case1.xls'
			self.sheet_id = 0
		self.data = self.get_data()

	#获取sheets的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	#写入数据
	def write_value(self,row,col,value):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(0)
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)

	#根据对应的caseid 找到对应行的内容
	def get_rows_data(self,case_id):
		row_num = self.get_row_num(case_id)
		rows_data = self.get_row_values(row_num)
		return rows_data

	#根据对应的caseid找到对应的行号
	def get_row_num(self,case_id):
		num = 0
		clols_data = self.get_cols_data()
		for col_data in clols_data:
			if case_id in col_data:
				return num
			num = num+1


	#根据行号，找到该行的内容
	def get_row_values(self,row):
		tables = self.data
		row_data = tables.row_values(row)
		return row_data

	#获取某一列的内容
	def get_cols_data(self,col_id=None):
		if col_id != None:
			cols = self.data.col_values(col_id)
		else:
			cols = self.data.col_values(0)
		return cols

	def get_xls(self, xls_name, sheet_name):  # xls_name填写用例的Excel名称 sheet_name该Excel的sheet名称
		cls = []
		# 获取用例文件路径
		xlsPath = os.path.join(path, "dataconfig",  xls_name)
		file = xlrd.open_workbook(xlsPath)  # 打开用例Excel
		# file = openpyxl.load_workbook(xlsPath)
		sheet = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet
		# sheet = file.get_sheet_names(sheet_name)
		# 获取这个sheet内容行数
		nrows = sheet.nrows
		for i in range(1,nrows):  # 根据行数做循环
			if sheet.row_values(i)[0] != u'case_name':  # 如果这个Excel的这个sheet的第i行的第一列不等于case_name那么我们把这行的数据添加到cls[]
				cls.append(sheet.row_values(i))
		return cls


if __name__ == '__main__':
	"""opers = OperationExcel()
	print(opers.get_cell_value(1,2))
	print(opers.get_lines())
	print(opers.get_xls("case1.xls","sheet1"))"""
	data = OperationExcel().get_xls("case1.xls", "sheet1")
	print(data[2])