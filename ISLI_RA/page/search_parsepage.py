import sys
sys.path.append("..")
from common import base
#RA的检索界面
#222222服务编码不存在

class Search_page(base.BasePage):
	# homepage_url =r"http://www.isli-international.org/irap/web/navigation/toNavigationPage/1"
	homepage_url =r"http://172.16.3.52:8080/irap/web/navigation/toNavigationPage/1"
	search_input_loc = ("css selector",'#bookNo1')														#首页输入框
	search_click_loc =("css selector",'#search1>input:nth-child(2)')										#首页确认按钮
	sum_loc = ("css selector",'.search-content>p')														#搜索结果总数显示
	search_detail_input_loc= ("css selector",'#bookNo2')													#结果页输入框
	search_detail_click_loc =("css selector",'#bookId')													#结果页确认按钮
	search_error_loc = ("css selector",'.errortip')														#搜索错误提示
	result_first_loc = ("css selector",'.search-list >div:nth-child(1)>a')								#搜索结果列表第一项
	return_button_loc = ("css selector",'#returnButton')													#详情界面返回按钮
	search_content_loc = ("css selector",'span.clearContent')											#详情结果页编码显示
	isli_code_table_loc=("css selector",'#islicode>div:nth-child(1)>h5')									#详情表单标题
	isli_code_loc =("css selector", '#islicode>div:nth-child(2)>table>tbody>tr:nth-child(1)>td')			#表单中编码显示

	def input_homecode(self,code):
		'''首页输入isli编码'''
		self.send_keys(self.search_input_loc,code)

	def click_search(self):
		'''首页确认搜索'''
		self.click(self.search_click_loc)

	def input_datailinput(self,code):
		'''结果页输入ISLI编码'''
		self.send_keys(self.search_detail_input_loc,code)

	def click_detail(self):
		'''结果页面确认搜索'''
		self.click(self.search_detail_click_loc)

	def get_searcheror_text(self):
		'''服务编码不存在提示'''
		return self.get_text(self.search_error_loc)

	def get_search_sum(self):
		'''搜索结果总数显示'''
		return self.get_text(self.sum_loc)

	def get_result_firsttext(self):
		'''获取搜索结果第一项的编码'''
		return self.get_text(self.result_first_loc)

	def click_resultfirst(self):
		'''查看搜索结果第一项目'''
		self.click(self.result_first_loc)

	def get_return_text(self):
		'''编码详细信息界面返回按钮'''
		return self.get_text(self.return_button_loc)

	def click_return(self):
		'''点击编码详细信息界面返回按钮'''
		self.click(self.return_button_loc)

	def get_search_islicode(self):
		'''编码详情页面右上角编码'''
		return self.get_text(self.search_content_loc)

	def get_table_name(self):
		'''编码详情页面表达title'''
		return self.get_text(self.isli_code_table_loc)

	def get_table_code(self):
		'''编码详情表单中islicode'''
		return self.get_text(self.isli_code_loc)

if __name__ =="__main__":
	pass
