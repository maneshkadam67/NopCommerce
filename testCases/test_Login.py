import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig

class TestLogin:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    # baseURL = "https://demo.nopcommerce.com/login?returnUrl=%2F"
    # username = "mkadam661@gmail.com"
    # password = "Manish@123"

    def test_homePageTitle(self,setup):
        self.driver=driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        pageTitle=self.driver.title

        if pageTitle=="nopCommerce demo store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            assert False
            self.driver.close()

    def test_login(self,setup):
        self.driver=driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lg=Login(self.driver)
        self.lg.setUserName(self.username)
        self.lg.setpassword(self.password)
        self.lg.clickLogin()
        pageTitle=self.driver.title

        if pageTitle=="nopCommerce demo store":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_login.png")
            assert False
            self.driver.close()








