import pytest
from selenium import webdriver


@pytest.fixture()
def initialize_driver():
	# creating a chrome session
	opts = webdriver.ChromeOptions()
	opts.add_experimental_option("detach", True)
	driver = webdriver.Chrome(options=opts)

	# launching the url
	url = "https://demo.actitime.com/login.do"
	driver.get(url)

	yield driver

	# closing the session
	driver.close()