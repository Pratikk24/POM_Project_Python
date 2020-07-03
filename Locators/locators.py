class Locators():
    # Login Page Objects :
    URL = "http://claim-portal-bajaj-dev.qa.i3systems.in/"
    username = "admin"
    password = "!3$y$+eMs"


    username_textbox_id = "id_username"
    password_textbox_id = "id_password"
    login_button_css_selector = "input[value=LOGIN]"

    # Title
    title = "Claim Assistant"

   # Document Page Objects
    Document_link_text = "DOCUMENT LIST"

    # Upload Documents :
    Upload_Document_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section/section[2]/section/button[1]"

    # Claim list page Objects :-
    Claims_list_link_text = "CLAIMS LIST"

    # select case
    Select_case = "/html/body/app-root/section/main/div/app-claims-list/section[2]/section[1]/table/tbody/tr[1]/td[1]/mat-checkbox/label/div"
    # down arrow for allocation
    Down_arrow_for_allocation = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[2]/section/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div"

    # selection of  qc user
    Selection_of_qc_user = "/html/body/div[2]/div[2]/div/div/div/mat-option[3]/span"


    # allocation of qc user
    Allocation_of_qc_user = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[2]/section/button[1]/span/mat-icon"


    # Logout from admin :
    Three_Dot_Icon = "//*[@id='header-main']/app-header/mat-toolbar/div[2]/ul[2]/li[3]/button/span/mat-icon"
    logout_x_path = "//*[@id='cdk-overlay-0']/div/div/button[2]/span"

     # login from qc user
    qc_username = "Ajit_QC_Bajaj"
    qc_password = "!3$y$+eMs"

   # Click on Case
    Open_Case_x_path = "//*[@id='i3tableId']/tbody/tr[1]"

    # Verify_Button
    Verify_Button_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]"

    # Logout from qc user:
    Three_Dot_Icon = "//*[@id='header-main']/app-header/mat-toolbar/div[2]/ul[2]/li[3]/button/span/mat-icon"
    logout_x_path = "/html/body/div[2]/div[2]/div/div/div/button[2]/span"
    output = 'C:/Users/VIJAYA/PycharmProjects/seleniump/pomproject/Reports'






