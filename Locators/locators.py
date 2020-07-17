class Locators():

    # executable_path
    executable_path = "C:/Users/VIJAYA/Desktop/webdrivers/chromedriver_win32/chromedriver"

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
    qc_username = "Ajit_QC_Bajaj"
    qc_password = "!3$y$+eMs"

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

    # Verify_Button
    verify_button_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]"


    # Title
    title = "Claim Assistant"

    # Report output Path
    output = 'C:/Users/VIJAYA/PycharmProjects/seleniump/pomproject/Reports'

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

    # clear date filter
    clear_date_filter = "/html/body/app-root/section/main/div/app-claims-list/section[1]/section/section[1]/section/mat-chip-list/div/section/mat-chip[3]/mat-icon"

    # open case
    open_case = "/html/body/app-root/section/main/div/app-claims-list/section[2]/section[1]/table/tbody/tr[1]/td[2]/section/span"

    # all doc icon
    all_doc_icon_x_path = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[1]/section[2]/button[1]/span/mat-icon"

    # all docs x path
    start = "/html/body/app-root/section/main/div/app-all-documents/section[2]/section[1]/section/mat-list/mat-list-item["
    end = "]/div/section/section[1]/h3/span"

    # back button from all doc
    back_button = "/html/body/app-root/section/main/div/app-all-documents/section[1]/section[1]/button[1]/span/mat-icon"



    # non_med_doc_details
    documeant_details = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[1]/div/app-qc-medical-details/section/mat-accordion/mat-expansion-panel[1]/mat-expansion-panel-header/span/mat-panel-title/span"

    # reports
    reports = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[1]/div/app-qc-medical-details/section/mat-accordion/mat-expansion-panel[2]/mat-expansion-panel-header/span/mat-panel-title/span"

    # med details
    medical_details_tab = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/mat-tab-header/div[2]/div/div/div[2]/div"

    # bills tab
    bills_tab = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]/div"

    # rurar
    scale = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[1]/section[2]/button[2]/span/mat-icon"
    # driver.execute_script("window.scrollBy(0,3000)", "")

    # close rurar
    close_scale = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[1]/section[2]/button[2]/span/mat-icon"

    # final bill
    aggregate_bill = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[1]/mat-button-toggle-group[1]/mat-button-toggle[2]/button/div/span[1]"
    # zoom in to ful screen activities
    startt = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[3]/section/section/mat-card/mat-card-content/section/div[1]/section/section/section[2]/section/button["
    endd = "]/span/mat-icon"

    # close full screen
    close_ful_screen = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[1]/section/app-document-view-page/section[4]/app-document-fullscreen-viewer/div/button/span/mat-icon"

   # final to pharma bill
    star = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[1]/mat-button-toggle-group["
    en = "]/mat-button-toggle[2]/button/div/span[1]"

    # npe to onp
    npe = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[1]/mat-button-toggle-group[10]/mat-button-toggle/button/div/span"
    st = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[3]/div/app-qc-bill-details/section/section[1]/section[2]/mat-button-toggle-group["
    e = "]/mat-button-toggle/button/div/span[1]"

    # financial_details
    financial_details = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/mat-tab-header/div[2]/div/div/div[4]/div"

    # pharma_detail
    pharma_detail = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[1]/div/div/section/section/mat-accordion/mat-expansion-panel/mat-expansion-panel-header/span/mat-panel-title/span"
    # pathology details
    patho_detail = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[1]/div/div/section/section/mat-accordion/mat-expansion-panel[3]/mat-expansion-panel-header/span/mat-panel-title/span"

    #pharmacy amount
    pharma_amount = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[1]/div/div/section/section/mat-accordion/mat-expansion-panel[1]/mat-expansion-panel-header/span/mat-panel-description/span"
    # pathology amount
    patho_amount = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[1]/div/div/section/section/mat-accordion/mat-expansion-panel[3]/mat-expansion-panel-header/span/mat-panel-description/span"
    # non payable summary amount
    nonp_amount = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[2]/div/div/section/section/mat-accordion/mat-expansion-panel[1]/mat-expansion-panel-header/span/mat-panel-description/span"
    # discount summary amount
    disc_amount = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[2]/div/div/section/section/mat-accordion/mat-expansion-panel[2]/mat-expansion-panel-header/span/mat-panel-description/span"
    # other deduction amount
    other_ded_amount = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[2]/div/div/section/section/mat-accordion/mat-expansion-panel[3]/mat-expansion-panel-header/span/mat-panel-description/span"

    # loop for all elements in deduction summary
    first = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/div/mat-tab-body[4]/div/app-qc-financial-details/section/mat-accordion/mat-expansion-panel[2]/div/div/section/section/mat-accordion/mat-expansion-panel["
    last = "]/mat-expansion-panel-header/span/mat-panel-title/span"

    # back to bills
    back_to_bills = "/html/body/app-root/section/main/div/app-qc-page/section/section/section[2]/section/mat-tab-group/mat-tab-header/div[2]/div/div/div[3]/div"

    # reprocess fs
    fs_reprocess = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[3]/button[2]/span/mat-icon"

    # back arrow icon
    back_arrow_x_path = "/html/body/app-root/section/main/div/app-qc-page/app-qc-header/section/section/section[1]/button/span/mat-icon"

    # Logout :
    three_dot_icon = "/html/body/app-root/section/header/app-header/mat-toolbar/div[2]/ul[2]/li[3]/button/span/mat-icon"
    logout_x_path = "/html/body/div[2]/div[2]/div/div/div/button[2]/span"







