from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import unittest

class Test_PythonOrg(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		sleep(4)
		self.browser.close()
		self.browser = None

	def _test_00_HomePageExists(self):
		"Test to make sure that the home page exists."
		self.browser.get("http://www.python.org")
		self.assertTrue("Python" in self.browser.title)			
	
	def _test_01_SearchEntryWorks(self):
		"Test that text entered in the search entry box gets results."
		self.browser.get("http://www.python.org")
		search_entry = self.browser.find_element_by_name("q")
		search_entry.clear()
		search_entry.send_keys("pycon")
		search_entry.send_keys(Keys.RETURN)
		self.assertTrue("No results found." not in self.browser.page_source)
		
	def test_02_LoginButtonGoesToLoginPage(self):
		"Test that when we click on the login button we go to the login page."
		self.browser.get("http://www.python.org")
		sign_in_button = self.browser.find_element_by_link_text("Sign In")
		sign_in_button.click()
		sleep(3)
		self.assertTrue("sign in to python" in self.browser.title.lower())			
if __name__ == "__main__":
	unittest.main(verbosity=2)


