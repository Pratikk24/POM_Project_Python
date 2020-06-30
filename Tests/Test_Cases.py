from selenium import webdriver
import time
import unittest
from Libraries.LIB_LoginPage import LoginPage
from Libraries.LIB_HomePage import HomePage
import HtmlTestRunner


class ClaimsTest(unittest.TestCase):
    URL = "https://ilgic-claim-al.i3systems.in/#/claims"
    username = "admin"
    password = "!3$y$+eMs"

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Driver/chromedriver_win32/chromedriver.exe")
        cls.driver.get(cls.URL)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()


    def test_01_Login_valid(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

        time.sleep(3)

    def test_02_Claim_list_Page_Validation(self):
        self.assertEqual("Claim Assistant", self.driver.title)

    def test_03_Navigate_to_Document_Page(self):
        driver = self.driver

        homePage = HomePage(driver)
        homePage.click_on_Document_list()

        time.sleep(2)

    def test_04_Click_on_Upload_Document(self):
         driver = self.driver

         homepage = HomePage(driver)
         homepage.click_on_Upload_Document()

         time.sleep(5)

    def test_05_Logout(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_Three_Dot_Icon()
        homepage.click_on_Logout()

        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Pratik/PycharmProjects/Claims-POM/Reports'))
