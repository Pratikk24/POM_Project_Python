from Locators.locators import Locators
from selenium.webdriver.common.by import By


class HomePage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        self.Three_Dot_Icon = Locators.Three_Dot_Icon
        self.Logout_x_path = Locators.logout_x_path
        self.Document_list = Locators.Document_link_text
        self.Upload_Document = Locators.Upload_Document_x_path

    # Functions or Action Methods

    def click_on_Document_list(self):
        self.driver.find_element_by_link_text(self.Document_list).click()

    def click_on_Upload_Document(self):
        self.driver.find_element_by_xpath(self.Upload_Document).click()

    def click_Three_Dot_Icon(self):
        self.driver.find_element_by_xpath(self.Three_Dot_Icon).click()

    def click_on_Logout(self):
        self.driver.find_element_by_xpath(self.Logout_x_path).click()












