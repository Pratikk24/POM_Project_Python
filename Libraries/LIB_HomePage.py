from Locators.locators import Locators


class Homepage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver

        self.three_dot_icon = Locators.three_dot_icon
        self.logout_x_path = Locators.logout_x_path
        self.document_list = Locators.document_link_text
        self.close_button = Locators.close_button_x_path
        self.refresh_button = Locators.refresh_button_x_path
        self.claims_list = Locators.claims_list_link_text
        self.select_case = Locators.select_case
        self.allocation_arrow = Locators.down_arrow_for_allocation
        self.qc_user_selection = Locators.selection_of_qc_user
        self.qc_user_allocation = Locators.allocation_of_qc_user
        self.open_case = Locators.open_case_x_path
        self.all_doc_icon = Locators.all_doc_icon_x_path
        self.back_arrow_button = Locators.back_arrow_x_path
        self.verify_button = Locators.verify_button_x_path

    # Functions or Action Methods

    def click_on_document_list(self):
        self.driver.find_element_by_link_text(self.document_list).click()

    def click_on_refresh_button(self):
        self.driver.find_element_by_xpath(self.refresh_button).click()

    def click_on_claims_list(self):
        self.driver.find_element_by_link_text(self.claims_list).click()

    def click_on_select_case(self):
        self.driver.find_element_by_xpath(self.select_case).click()

    def click_on_allocation_arrow(self):
        self.driver.find_element_by_xpath(self.allocation_arrow).click()

    def click_on_qc_user_selection(self):
        self.driver.find_element_by_xpath(self.qc_user_selection).click()

    def click_on_qc_user_allocation(self):
        self.driver.find_element_by_xpath(self.qc_user_allocation).click()

    def open_case_by_clicking(self):
        self.driver.find_element_by_xpath(self.open_case).click()

    def click_on_all_doc_icon(self):
        self.driver.find_element_by_xpath(self.all_doc_icon).click()

    def click_all_doc_tabs(self):
        for i in range(1, 25):
            self.driver.find_element_by_xpath(Locators.start+str(i)+Locators.end ).click()

    def click_back_button(self):
         self.driver.find_element_by_xpath(self.back_arrow_button).click()

    def verify_case(self):
        self.driver.find_element_by_xpath(self.verify_button).click()

    def click_on_three_dot_icon(self):
        self.driver.find_element_by_xpath(self.three_dot_icon).click()

    def click_on_logout(self):
        self.driver.find_element_by_xpath(self.logout_x_path).click()
