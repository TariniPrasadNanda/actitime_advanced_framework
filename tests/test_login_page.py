from datetime import datetime
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source_page.login_page import LoginPage

data = [("admin", "manage"), ("admin", "trainee"), ("trainee", "trainee")]


@pytest.mark.parametrize("username, password", data)
def test_login(initialize_driver, username, password):
	driver = initialize_driver
	try:
		lp = LoginPage(driver)
		lp.enter_username(username)
		lp.enter_password(password)
		lp.click_login_btn()
		# get screenshot
		wait_ = WebDriverWait(driver, 10)

		# # validating login through url
		# wait_.until(EC.url_to_be("https://demo.actitime.com/user/submit_tt.do"))

		# validate through title
		wait_.until(EC.title_is("actiTIME - Enter Time-Track"))


	except Exception as error_msg:
		# driver.get_screenshot_as_file()
		td = datetime.now()
		path = r"C:\Users\Vidyashree M C\PycharmProjects\framework_actitime\screenshots\\"
		name = f"{__name__}-{td.day}-{td.month}-{td.year}-{td.hour}-{td.minute}-{td.second}.png"
		driver.save_screenshot(path + name)
		raise error_msg


"""
1. take out excel function in login_page.py into excel_library.py
2. create a fixture for launching the session and closing the session
	in test_login_page.py
3. get the driver from fixture into test_login() and from this test_login()
   pass it to class LoginPage():
4. for executing: pytest test_login_page.py -vs

-----------------------------------------------------------------------
5. move fixture from test_login_page.py to conftest.py
6. create folder structure.
7. reports folder --> 
pytest test_login_page.py -vs --html="C:/Users/Vidyashree M C/PycharmProjects/framework_actitime/reports/reportname.html"

"""



