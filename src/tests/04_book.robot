*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  data_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page


*** Test Cases ***

Add New Book Without Author
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_1}
    Submit Login Credentials    
    Click Link  Lisää kirja
    Set Booktitle  ${test_title}
    Set ISBN  ${test_isbn}
    Set Description  ${test_description}
    Click Element  submit
    Page Should Contain  Lisää uusi kirja
    
Add New Book Without Title
    Go To Home Page
    Click Link  Lisää kirja
    Set Writer  ${test_author}
    Set ISBN  ${test_isbn}
    Set Description  ${test_description}
    Click Element  submit
    Page Should Contain  Lisää uusi kirja

Add New Book Into List
    Click Link  Lisää kirja
    Set Writer  ${test_author}
    Set Booktitle  ${test_title}
    Set ISBN  ${test_isbn}
    Set Description  ${test_description}    
    Click Element  submit
    Page Should Contain  Lukuvinkkilista
    
Add New Book Without Additional Info
    Click Link  Lisää kirja
    Set Writer  ${test_author_2}
    Set Booktitle  ${test_title_2}
    Click Element  submit
    Page Should Contain  Lukuvinkkilista
