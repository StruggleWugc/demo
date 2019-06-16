import sys
# sys.path.append("..")
from page.search_parsepage import Search_page
import unittest,time

class Search_test(unittest.TestCase):
	'''RA官网解析'''
	@classmethod
	def setUpClass(cls):
		cls.driver = Search_page()
		cls.driver.open(Search_page.homepage_url)

	def test_01(self):
		'''首页输入框输入存在的关键词进行搜索'''
		self.driver.input_homecode('2')
		self.driver.click_search()
		time.sleep(5)
		self.assertTrue(self.driver.is_visibility(('css selector','.pageBox span')))
		# self.assertEqual('共3,308条检索结果',self.driver.get_search_sum())
		self.driver.click(('css selector','.logo'))

	def test_02(self):
		'''首页输入存在的中文关键词'''
		time.sleep(0.5)
		self.driver.input_homecode('科技')
		self.driver.click_search()
		time.sleep(5)
		self.assertTrue(self.driver.is_visibility(('css selector','.pageBox span')))
		# self.assertEqual('共997条检索结果',self.driver.get_search_sum())
		self.driver.click(('css selector','.logo'))

	def test_03(self):
		'''输入不存在的编码'''
		time.sleep(1)
		self.driver.input_homecode('222222')
		self.driver.click_search()
		time.sleep(3)
		self.assertEqual('服务编码不存在',self.driver.get_searcheror_text())

	def test_04(self):
		'''搜索结果界面进行搜索'''
		self.driver.input_datailinput('2')
		self.driver.click_detail()
		time.sleep(3)
		self.assertTrue(self.driver.is_visibility(('css selector','.pageBox span')))
		# self.assertEqual('共3,308条检索结果',self.driver.get_search_sum())

	def test_05(self):
		'''查看详情至返回'''
		a =self.driver.get_result_firsttext()
		self.driver.click_resultfirst()
		time.sleep(2)
		self.assertEqual("服务编码元数据",self.driver.get_table_name())					#断言表头
		self.assertEqual("<<返回",self.driver.get_return_text())						#断言返回按钮
		self.assertEqual(a,self.driver.get_search_islicode())							#断言详情列表右上角code
		self.assertIn(self.driver.get_table_code(),a)									#断言详情列表code
		self.driver.click_return()
		d =self.driver.is_exists(Search_page.search_detail_input_loc)
		self.assertTrue(d)																#断言页面存在输入框

	def test_06(self):
		'''输入完整code进行解析'''
		self.driver.input_datailinput('000000-000000000303527-2')
		self.driver.click_detail()
		a =self.driver.get_attribute((Search_page.search_detail_input_loc),'value')
		time.sleep(2)
		self.assertEqual(a,self.driver.get_table_code())
		self.assertIn(a,self.driver.get_search_islicode())
	@classmethod
	def tearDownClass(cls):
		cls.driver.close()


if __name__ =="__main__":
	unittest.main()