from selenium import webdriver
import time
import unittest
from pomproject.pages.loginpage import LoginPage
from pomproject.pages.homepage import HomePage
from pomproject.locators.locators import Locators
import HtmlTestRunner
import autoit


class ClaimsTest(unittest.TestCase):
    Url = Locators.URL
    Username = Locators.username
    Password = Locators.password






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

    def file_upload(self):
        
        autoit.win_wait_active("Open", 10)
        autoit.control_send("Open", "Edit1", "sampleupload10")
        autoit.control_click("Open", "Button1")
        time.sleep(20)

    #def test_04_Click_on_Upload_file(self):

         #driver = self.driver

        # homepage = HomePage(driver)
         #homepage.click_on_upload_file()

         #time.sleep(20)

    #def test_05_case_state_validation(self):
       # self.assertEqual("File O210328221-007.zip uploaded successfully!",self.driver.find_element_by_xpath(Locators.assertion_upcase))


    def test_06_Go_to_claim_list_page(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_on_Claims_list()

        time.sleep(3)

    def test_07_Open_case_by_clicking(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.Open_case_by_clicking()
        time.sleep(4)

    def test_08_Verify_Case(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.Verify_case()
        time.sleep(3)

    #def test_09_assertion_verify_case(self):
       #self.assertEqual("File O210328221-007.zip uploaded successfully!",self.driver.find_element_by_xpath(Locators.assertion_verify_case))

    def test_10_Logout(self):
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











