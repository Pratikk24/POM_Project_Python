class Locators():
    # Login Page Objects :
    URL = "http://claim-portal-bajaj-dev.qa.i3systems.in/"
    username = "admin"
    password = "!3$y$+eMs"

   # wait = "Open"
    #control = "Open"
  #  send = "Edit1"
   # filename = "sampleupload10"
   # controls = "Open"
   # click = "Button1"


    #assertion_upcase = "/html/body/app-root/section/main/div/app-document-list/section[1]/section[2]/app-material-file-upload/section/section[2]/mat-list/mat-list-item/div/div[2]/p/span[3]"
   # assertion_verify_case = ""


    username_textbox_id = "id_username"
    password_textbox_id = "id_password"
    login_button_css_selector = "input[value=LOGIN]"

   # Document Page Objects
    Document_link_text = "DOCUMENT LIST"

    # Upload Documents :
    Upload_Document_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section/section[2]/section/button[1]"

    # Claim list page Objects :-
    Claims_list_link_text = "CLAIMS LIST"

    # Click on Case
    Open_Case_x_path = "//*[@id='i3tableId']/tbody/tr[1]"

    # Verify_Button
    Verify_Button_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]"

    # Logout :
    Three_Dot_Icon = "//*[@id='header-main']/app-header/mat-toolbar/div[2]/ul[2]/li[3]/button/span/mat-icon"
    logout_x_path = "//*[@id='cdk-overlay-0']/div/div/button[2]/span"
    output = 'C:/Users/VIJAYA/PycharmProjects/seleniump/pomproject/report'

    # Title
    title = "Claim Assistant"

