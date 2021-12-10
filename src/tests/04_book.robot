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
    
Add New Book By ISBN
    Click Link  Lisää kirja
    Click Element  xpath://a[@href="/search_isbn"]
    Set ISBN  ${test_isbn_3}
    Click Element  submit
    Page Should Contain  Otsikko: ${test_title_3}
    
Add New Book By Invalid ISBN
    Click Link  Lisää kirja
    Click Element  xpath://a[@href="/search_isbn"]
    Set ISBN  756756-232323
    Click Element  submit
    Page Should Contain  No info found with this ISBN

Book Is Found From List
    Go To Home Page
    Page Should Contain  Otsikko: ${test_title}
    
Book Is Not Marked As Read
    Element Should Contain  //*[@id="${test_title}_"]  Luettu: None

Mark Book As Read
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_title}"]
    Click Button  Merkitse luetuksi
    ${time_now}=  Get Current Date  result_format=%Y-%m-%d %H:%M
    Element Should Contain  //*[@id="${test_title}_"]  ${time_now}
