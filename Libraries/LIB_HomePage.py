from Locators.locators import Locators


class Homepage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver


        self.document_list = Locators.document_link_text
        self.close_button = Locators.close_button_x_path
        self.refresh_button = Locators.refresh_button_x_path
        self.claims_list = Locators.claims_list_link_text
        self.select_case = Locators.select_case
        self.allocation_arrow = Locators.down_arrow_for_allocation
        self.qc_user_selection = Locators.selection_of_qc_user
        self.qc_user_allocation = Locators.allocation_of_qc_user
        self.clear_date_filter = Locators.clear_date_filter

        self.open_case = Locators.open_case_x_path
        self.all_doc_icon = Locators.all_doc_icon_x_path
        self.back_button = Locators.back_button

        self.doc_details = Locators.documeant_details
        self.reports = Locators.reports
        self.medical_details = Locators.medical_details_tab
        self.bills_tab = Locators.bills_tab

        self.scale = Locators.scale
        self.close_scale = Locators.close_scale

        self.final_bill = Locators.aggregate_bill
        self.close_fulscreen = Locators.close_ful_screen

        self.startt = Locators.startt
        self.endd = Locators.endd
        self.npe = Locators.npe
        self.st = Locators.st
        self.e = Locators.e
        self.fs = Locators.financial_details
        self.pharma_details = Locators.pharma_detail
        self.patho_details = Locators.patho_detail

        self.pharma_amount = Locators.pharma_amount
        self.patho_amount = Locators.patho_amount
        self.nonp_amount = Locators.nonp_amount
        self.discount_summary = Locators.disc_amount
        self.other_deduction = Locators.other_ded_amount

        self.first = Locators.first
        self.last = Locators.last

        self.back_to_bills = Locators.back_to_bills
        self.fs_reprocess = Locators.fs_reprocess
        self.back_arrow_button = Locators.back_arrow_x_path
        self.verify_button = Locators.verify_button_x_path

        self.three_dot_icon = Locators.three_dot_icon
        self.logout_x_path = Locators.logout_x_path

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

    def click_clear_date_filter(self):
        self.driver.find_element_by_xpath(self.clear_date_filter).click()

    def open_case_by_clicking(self):
        self.driver.find_element_by_xpath(self.open_case).click()

    def click_on_all_doc_icon(self):
        self.driver.find_element_by_xpath(self.all_doc_icon).click()

    def click_all_doc_tabs(self):
        for i in range(1, 25):
            self.driver.find_element_by_xpath(Locators.start + str(i) + Locators.end).click()

    def click_back_button(self):
        self.driver.find_element_by_xpath(self.back_button).click()

    def click_doc_details(self):
        self.driver.find_element_by_xpath(self.doc_details).click()

    def click_reports(self):
        self.driver.find_element_by_xpath(self.reports).click()

    def click_on_medical_details(self):
        self.driver.find_element_by_xpath(self.medical_details).click()

    def click_on_bills_tabs(self):
        self.driver.find_element_by_xpath(self.bills_tab).click()

    def click_on_scale(self):
        self.driver.find_element_by_xpath(self.scale).click()
        self.driver.execute_script("window.scrollBy(0,10000)", "")

    def click_on_close_scale(self):
        self.driver.find_element_by_xpath(self.close_scale).click()

    def click_on_final_bill(self):
        self.driver.find_element_by_xpath(self.final_bill).click()
        a = [1, 2, 3, 4, 5, 6]
        for i in a:
            self.driver.find_element_by_xpath(Locators.startt + str(i) + Locators.endd).click()

    def click_on_close_fulscreen(self):
        self.driver.find_element_by_xpath(self.close_fulscreen).click()
        b = [2, 3]
        for i in b:
            self.driver.find_element_by_xpath(Locators.star + str(i) + Locators.en).click()

    def click_npe(self):
        self.driver.find_element_by_xpath(self.npe).click()
        c = [5, 6]
        for i in c:
            self.driver.find_element_by_xpath(Locators.st + str(i) + Locators.e).click()

    def click_on_fs(self):
        self.driver.find_element_by_xpath(self.fs).click()

    def click_on_pharma_details(self):
        self.driver.find_element_by_xpath(self.pharma_details).click()

    def click_patho_details(self):
        self.driver.find_element_by_xpath(self.patho_details)
        d = [1, 2, 3]
        for i in d:
            self.driver.find_element_by_xpath(Locators.first + str(i) + Locators.last).click()

    def click_pharma_amount(self):
        pharma_value = self.driver.find_element_by_xpath(self.pharma_amount)
        amount = pharma_value.text
        print(amount)


    def get_patho_amount(self):
        patho_amount = self.driver.find_element_by_xpath(self.patho_amount)
        value = patho_amount.text
        print(value)

    def get_nonp_amount(self):
        nonp_amount = self.driver.find_element_by_xpath(self.nonp_amount)
        price = nonp_amount.text
        print(price)

    def get_dis_summary(self):
        dis_amount = self.driver.find_element_by_xpath(self.discount_summary)
        price = dis_amount.text
        print(price)

    def get_other_deduction(self):
        other_ded_amount = self.driver.find_element_by_xpath(self.other_deduction)
        price = other_ded_amount.text
        print(price)

    def click_on_back_to_bills(self):
        self.driver.find_element_by_xpath(self.back_to_bills).click()

    def click_on_fs_reprocess(self):
        self.driver.find_element_by_xpath(self.fs_reprocess).click()

    def click_back_arrow(self):
         self.driver.find_element_by_xpath(self.back_arrow_button).click()

    def verify_case(self):
        self.driver.find_element_by_xpath(self.verify_button).click()

    def click_on_three_dot_icon(self):
        self.driver.find_element_by_xpath(self.three_dot_icon).click()

    def click_on_logout(self):
        self.driver.find_element_by_xpath(self.logout_x_path).click()
        
        
