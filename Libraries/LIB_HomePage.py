from Locators.locators import Locators


class HomePage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver


        self.Three_Dot_Icon = Locators.Three_Dot_Icon
        self.Logout_x_path = Locators.logout_x_path
        self.Document_list = Locators.Document_link_text
        self.Upload_Document = Locators.Upload_Document_x_path
        self.Claims_list = Locators.Claims_list_link_text
        self.Select_case = Locators.Select_case
        self.Allocation_arrow = Locators.Down_arrow_for_allocation
        self.Qc_user_selection = Locators.Selection_of_qc_user
        self.Qc_user_allocation = Locators.Allocation_of_qc_user
        self.Three_Dot_Icon = Locators.Three_Dot_Icon
        self.Logout_x_path = Locators.logout_x_path
        self.Open_case = Locators.Open_Case_x_path
        self.Verify_button = Locators.Verify_Button_x_path

    # Functions or Action Methods

    def click_on_Document_list(self):
        self.driver.find_element_by_link_text(self.Document_list).click()

    def click_on_Upload_Document(self):
        self.driver.find_element_by_xpath(self.Upload_Document).click()

    def click_on_select_case(self):
        self.driver.find_element_by_xpath(self.Select_case).click()

    def click_on_allocation_arrow(self):
        self.driver.find_element_by_xpath(self.Allocation_arrow).click()

    def click_on_qc_user_selection(self):
        self.driver.find_element_by_xpath(self.Qc_user_selection).click()

    def click_on_qc_user_allocation(self):
        self.driver.find_element_by_xpath(self.Qc_user_allocation).click()

    def click_Three_Dot_Icon(self):
        self.driver.find_element_by_xpath(self.Three_Dot_Icon).click()

    def click_on_Logout(self):
        self.driver.find_element_by_xpath(self.Logout_x_path).click()

    def click_on_Claims_list(self):
        self.driver.find_element_by_link_text(self.Claims_list).click()

    def Open_case_by_clicking(self):
        self.driver.find_element_by_xpath(self.Open_case).click()

    def Verify_case(self):
        self.driver.find_element_by_xpath(self.Verify_button).click()











