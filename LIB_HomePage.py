from pomproject.locators.locators import Locators
import autoit



class HomePage():

    # Constructor
    def __init__(self, driver):
        self.driver = driver


        self.Three_Dot_Icon = Locators.Three_Dot_Icon
        self.Logout_x_path = Locators.logout_x_path
        self.Document_list = Locators.Document_link_text
        self.Upload_Document = Locators.Upload_Document_x_path
        self.Claims_list = Locators.Claims_list_link_text
        self.Open_case = Locators.Open_Case_x_path
        self.Verify_button = Locators.Verify_Button_x_path

        #self.wait_command = Locators.wait
        #self.control_command = Locators.control
        #self.send_command = Locators.send
        #self.filename_command = Locators.filename
        #self.controls_command = Locators.controls
       # self.click_command = Locators.click

    # Functions or Action Methods

    def click_on_Document_list(self):
        self.driver.find_element_by_link_text(self.Document_list).click()

    def click_on_Upload_Document(self):
        self.driver.find_element_by_xpath(self.Upload_Document).click()

    #def click_on_upload_file(self):
        #self.driver.autoit.win_wait_active(self.wait_command,4)
       # self.driver.autoit.control_send(self.control_command,self.send_command,self.filename_command)
        #self.driver.autoit.control_click(self.controls_command,self.click_command)

    def click_on_Claims_list(self):
        self.driver.find_element_by_link_text(self.Claims_list).click()

    def Open_case_by_clicking(self):
        self.driver.find_element_by_xpath(self.Open_case).click()

    def Verify_case(self):
        self.driver.find_element_by_xpath(self.Verify_button).click()

    def click_Three_Dot_Icon(self):
        self.driver.find_element_by_xpath(self.Three_Dot_Icon).click()

    def click_on_Logout(self):
        self.driver.find_element_by_xpath(self.Logout_x_path).click()


