from selenium import webdriver
import time
import unittest
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_01_login_valid(self):
        driver = self.driver

        driver.get("http://datamd-md-india.qa.i3systems.in/")

        login = LoginPage(driver)
        login.enter_username("admin")
        login.enter_password("!3$y$+eMs")
        login.click_login()
        self.assertEqual("Underwrite Assistant", self.driver.title, "Wabepage title is not matching")

        homepage = HomePage(driver)
        homepage.click_Down_Caret_Icon()
        homepage.click_logout()

        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Pratik/PycharmProjects/POMproject/Reports'))









