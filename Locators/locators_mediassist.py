class Locators():

    # executable_path
    executable_path = "C:/Driver/chromedriver_win32/chromedriver.exe"

    # url :
    url = "http://claim-portal-mediassist.qa.i3systems.in/"

    # Login Page Objects :
    username_textbox_id = "id_username"
    password_textbox_id = "id_password"
    login_button_css_selector = "input[value=LOGIN]"

    # username & password
    Username = "admin"
    Password = "!3$y$+eMs"

    # qc_username & Password :
    qc_username = "qc_user"
    qc_password = "!3$y$+eMs"

    # Home Page Objects :-

    # Document Page Objects
    document_link_text = "DOCUMENT LIST"

    # Claim list page Objects :-
    claims_list_link_text = "CLAIMS LIST"

    # select case
    select_case = "/html/body/app-root/section/main/div/app-claims-list/section[2]/section[1]/table/tbody/tr[1]/td[1]/mat-checkbox/label/div"

    # down arrow for allocation
    down_arrow_for_allocation = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[2]/section/mat-form-field/div/div[1]/div/mat-select/div/div[2]/div"

    # selection of  qc user
    selection_of_qc_user = "/html/body/div[2]/div[2]/div/div/div/mat-option[2]/span"

    # allocation of qc user
    allocation_of_qc_user = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[2]/section/button[1]/span/mat-icon"

    # Click on Case
    open_case_x_path = "/html/body/app-root/section/main/div/app-claims-list/section[2]/section[1]/table/tbody/tr[1]"

    #claim page edit button
    edit_button = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[1]/span/span"

    # claim page save button
    save_button = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]/span/span"

    #claim page cancel button
    cancel_button = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[1]/span/span"

    # doc_details
    documeant_details = "//*[@id='mat-expansion-panel-header-45']/span/mat-panel-title/span"

    # claim details
    claim_details = "//*[@id='mat-expansion-panel-header-46']/span/mat-panel-title"

    # reports
    reports = "//*[@id='mat-expansion-panel-header-47']/span/mat-panel-title/span"

    # med details tab
    medical_details_tab = "//*[@id='mat-tab-label-2-1']/div"

    # Medical details summary
    medical_details_summary = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[2]/div/app-qc-medical-details/section/mat-accordion/mat-expansion-panel[1]/mat-expansion-panel-header/span/mat-panel-title/span"

    # Hospital Details Summary
    hospital_details_summary = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[2]/div/app-qc-medical-details/section/mat-accordion/mat-expansion-panel[2]/mat-expansion-panel-header/span/mat-panel-title/span"

    # bills tab
    bills_tab = "//*[@id='mat-tab-label-2-2']/div"

    # rurar
    ruler = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[1]/section[2]/button[2]/span/mat-icon"

    # close rurar
    close_ruler = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[1]/section[2]/button[2]/span/mat-icon"

    # final bill
    aggregate_bill = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[1]/mat-button-toggle-group[1]/mat-button-toggle[2]/button/div/span[1]"


    document_view_start = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[3]/section/section/mat-card/mat-card-content/section/div[1]/section/section/section[2]/section/button["
    document_view_end = "]/span/mat-icon"

    # close full screen
    close_full_screen = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[4]/app-document-fullscreen-viewer/div/button/span/mat-icon"

    # aggregate to pharma bill
    bill_start = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[1]/mat-button-toggle-group["
    bill_end = "]/mat-button-toggle[2]/button/div/span[1]"

    #Prepost tab
    prepost = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[2]/mat-button-toggle-group[5]/mat-button-toggle/button/div/span[1]"

    # Other np
    other_np = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[2]/mat-button-toggle-group[6]/mat-button-toggle/button/div/span[1]"


    # financial_details
    financial_details = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/mat-tab-header/div[2]/div/div/div[4]/div"

    # npe to other deduction
    first = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[2]/div/div/section/section/mat-accordion/mat-expansion-panel["
    last = "]/mat-expansion-panel-header/span/mat-panel-title/span"

    # Verify_Button
    verify_button_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]"

    # Reject_button
    reject_button_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[3]/span/mat-icon"

    # Logout :
    three_dot_icon = "//*[@id='header-main']/app-header/mat-toolbar/div[2]/ul[2]/li[3]/button/span/mat-icon"
    logout_x_path = "/html/body/div[2]/div[2]/div/div/div/button[3]/span"

    # Title
    title = "Claim Assistant"

    # Report output Path
    output = 'C:/Users/Pratik/PycharmProjects/claim-portal-Mediassist/Reports'

    # Close Button
    close_button_x_path = "//*[@id='file-upload-section']/app-material-file-upload/section/section[1]/button[2]/span/mat-icon"

    # Refresh Button
    refresh_button_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section/section[2]/section/button[3]"

    # Case state
    case_state_x_path = "//*[@id='i3tableId']/tbody/tr[1]/td[3]/section/span"

    # state
    state = "Case Created"

    # Document Upload Successfully
    upload_successfully_x_path = "/html/body/app-root/section/main/div/app-document-list/section[1]/section[2]/app-material-file-upload/section/section[2]/mat-list/mat-list-item/div/div[2]/p/span[3]"

    # Upload successfully message
    upload_successfully_text = "File o210328230-14.jpg uploaded successfully!"

    #all doc icon
    all_doc_icon_x_path = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[1]/section[2]/button[1]/span/mat-icon"

    # all docs x path
    start = "/html/body/app-root/section/main/div/app-all-documents/section[2]/section[1]/section/mat-list/mat-list-item["
    end = "]/div/section/section[1]/h3/span"

    # back arrow icon
    back_arrow_x_path = "/html/body/app-root/section/main/div/app-all-documents/section[1]/section[1]/button[1]/span/mat-icon"








