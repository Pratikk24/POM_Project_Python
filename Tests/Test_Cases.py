from selenium import webdriver
import time
import unittest
from Libraries.LIB_LoginPage import LoginPage
from Libraries.LIB_HomePage import HomePage
from Locators.locators import Locators
import HtmlTestRunner



class ClaimsTest(unittest.TestCase):
    Url = Locators.URL
    Username = Locators.username
    Password = Locators.password
    Qc_username = Locators.qc_username
    Qc_password = Locators.qc_password





    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/VIJAYA/Desktop/webdrivers/chromedriver_win32/chromedriver")

        cls.driver.get(cls.Url)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()



    def test_01_Login_valid(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username(self.Username)
        login.enter_password(self.Password)
        login.click_login()

        time.sleep(3)

    def test_02_Claim_list_Page_Validation(self):
        self.assertEqual(Locators.title, self.driver.title)

    def test_03_Navigate_to_Document_Page(self):
        driver = self.driver

        homePage = HomePage(driver)
        homePage.click_on_Document_list()

        time.sleep(2)

    def test_04_Click_on_Upload_Document(self):
         driver = self.driver

         homepage = HomePage(driver)
         homepage.click_on_Upload_Document()

         time.sleep(25)




    def test_05_Go_to_claim_list_page(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_on_Claims_list()

        time.sleep(3)

    def test_06_select_case(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_on_select_case()
        time.sleep(2)

    def test_07_allocation_arrow(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_on_allocation_arrow()
        time.sleep(2)

    def test_08_qc_user_selection(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_on_qc_user_selection()
        time.sleep(2)

    def test_09_qc_user_allocqtion(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_on_qc_user_allocation()
        time.sleep(2)

    def test_10_Logout(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_Three_Dot_Icon()
        homepage.click_on_Logout()

        time.sleep(3)

    def test_11_qc_user_login_validation(self):
        driver = self.driver

        login = LoginPage(driver)
        login.enter_username(self.Qc_username)
        login.enter_password(self.Qc_password)
        login.click_login()

        time.sleep(4)


    def test_12_Open_case_by_clicking(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.Open_case_by_clicking()
        time.sleep(4)

    def test_13_Verify_Case(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.Verify_case()
        time.sleep(3)

    def test_14_Logout_from_qc_user(self):
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
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(Locators.output))

