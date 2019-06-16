import xlrd
class Read(object):
	def __init__(self,excelpath,sheetindex=0):
		'''index定位sheet'''
		self.data = xlrd.open_workbook(excelpath).sheet_by_index(int(sheetindex))
		# self.table = self.data.sheet_by_index(int(sheetindex))

	def read_cell(self,x,y):
		'''指定坐标获取'''
		data =self.data.cell_value(x,y)
		return data

	def read_rows(self,row):
		'''整行'''
		data = self.data.row_values(row)
		return data

	def read_cols(self,col):
		'''整列'''
		data = self.data.col_values(col)
		return data

	def read_data(self,row=0,col=0,type=False):
		if row ==0 and col ==0:
			return
		elif row ==0 or col ==0:
			if row ==0:
				data = self.data.col_values(col)		#列
				return data
			else:
				data = self.data.col_values(row)		#行
				return data
		else:
			if type:
				data = self.data.cell_type(row,col)
				return data
			else:
				datatype =self.data.cell_value(row,col)
				return datatype

	def read_datanum(self,rows =0,cols=0):
		if rows ==0:
			return self.data.ncols				#列数
		else:
			return self.data.nrows				#行数



if __name__ =="__main__":
	data = Read('D:\BaiduNetdiskDownload\ISLI_RA\date\ISLI_RA_MS.xls')
	print(data.read_rows(2)[0])
	# print data.read_rows(2)
	# print(type(data.read_rows(2)))
