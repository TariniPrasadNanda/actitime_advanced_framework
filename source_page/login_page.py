import time
from generic.excel_library import read_locators

loc_file_path = r"C:\Users\Vidyashree M C\PycharmProjects\framework_actitime\project_files\actitime_locators.xlsx"
login_sheet_name = "login_objects"


class LoginPage:
	""" This class hold all the functionalities of login page """
	locators = read_locators(loc_file_path, login_sheet_name)


	def __init__(self, driver):
		self.driver = driver

	def enter_username(self, username):
		""" entering username in username textfield """
		self.driver.find_element(*self.locators["username_txt"]).send_keys(username)
		time.sleep(2)

	def enter_password(self, password):
		"""entering password in password textfield"""
		self.driver.find_element(*self.locators["password_txt"]).send_keys(password)
		time.sleep(2)

	def click_login_btn(self):
		"""click on login button"""
		self.driver.find_element(*self.locators["login_btn"]).click()
		time.sleep(2)



