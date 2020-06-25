from Locators.locators import Locators

class HomePage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        self.Down_Caret_Icon = Locators.Down_Caret_Icon
        self.logout_link_linktext = Locators.logout_link_linktext

    # Functions or Action Methods

    def click_Down_Caret_Icon(self):
        self.driver.find_element_by_id(self.Down_Caret_Icon).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()









