class Locators():

    # executable_path
    executable_path = "C:/Driver/chromedriver_win32/chromedriver.exe"

    # url :
    url = "http://claim-portal-bajaj-dev.qa.i3systems.in/"

    # Login Page Objects :
    username_textbox_id = "id_username"
    password_textbox_id = "id_password"
    login_button_css_selector = "input[value=LOGIN]"

    # username & password
    Username = "admin"
    Password = "!3$y$+eMs"

    # qc_username & Password :
    qc_username = "qc_user1"
    qc_password = "!3$y$+eMs"

    # Home Page Objects :-

    # Document Page Objects
    document_link_text = "DOCUMENT LIST"

    # Upload Documents :
    upload_document_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section/section[2]/section/button[1]"

    # Claim list page Objects :-
    claims_list_link_text = "CLAIMS LIST"

    # select case
    select_case = "/html/body/app-root/section/main/div/app-claims-list/section[2]/section[1]/table/tbody/tr[1]/td[1]/mat-checkbox/label/div"

    # down arrow for allocation
    down_arrow_for_allocation = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[2]/section/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div"

    # selection of  qc user
    selection_of_qc_user = "/html/body/div[2]/div[2]/div/div/div/mat-option[3]/span"

    # allocation of qc user
    allocation_of_qc_user = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[2]/section/button[1]/span/mat-icon"

    # Click on Case
    open_case_x_path = "//*[@id='i3tableId']/tbody/tr[1]"

    # Verify_Button
    verify_button_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]"

    # Logout :
    three_dot_icon = "//*[@id='header-main']/app-header/mat-toolbar/div[2]/ul[2]/li[3]/button/span/mat-icon"
    logout_x_path = "//*[@id='cdk-overlay-0']/div/div/button[2]/span"

    # Title
    title = "Claim Assistant"

    # Report output Path
    output = 'C:/Users/Pratik/PycharmProjects/Claims-POM/Reports'

    # Close Button
    close_button_x_path = "//*[@id='file-upload-section']/app-material-file-upload/section/section[1]/button[2]/span/mat-icon"

    # Refresh Button
    refresh_button_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section/section[2]/section/button[3]"

    # file name path
    file_name_x_path = "//*[@id='i3tableId']/tbody/tr[1]/td[2]/section/span"

    # file name
    file_name = "o210328230-14.jpg"

    # Case state
    case_state_x_path = "//*[@id='i3tableId']/tbody/tr[1]/td[3]/section/span"

    # state
    state = "Case Created"

    # Document Upload Successfully
    upload_successfully_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section[2]/app-material-file-upload/section/section[2]/mat-list/mat-list-item/div/div[2]/p/span[3]"

    # Upload successfully message
    upload_successfully_text = "File o210328230-14.jpg uploaded successfully!"
