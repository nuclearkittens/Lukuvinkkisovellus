*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  data_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page


*** Test Cases ***

Login And Go To Tag Page
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_1}
    Submit Login Credentials    
    Click Link  Hallinnoi tageja
    Page Should Contain  Lisää uusi tagi

Add New Tag With Valid Name
    Go To Home Page
    Click Link  Hallinnoi tageja
    Set Tag Name  ${test_tagname}
    Click Element  submit
    Page Should Contain  ${test_tagname}

Add New Tag With Too Short Name
    Go To Home Page
    Click Link  Hallinnoi tageja
    Set Tag Name  ${test_tagname_2}
    Click Element  submit
    Page Should Contain  ${test_tagname}
    Page Should Not Contain  ${test_tagname_2}

Delete Tag From The List
    Go To Home Page
    Click Link  Hallinnoi tageja
    Click Element  xpath://*[@id="${test_tagname}"]
    Page Should Not Contain  ${test_tagname}  

Add Multiple Tags With Valid Names
    Go To Home Page
    Click Link  Hallinnoi tageja
    Set Tag Name  ${test_tagname_3}
    Click Element  submit
    Set Tag Name  ${test_tagname_4}
    Click Element  submit
    Set Tag Name  ${test_tagname_5}
    Click Element  submit
    Page Should Contain  ${test_tagname_3}
    Page Should Contain  ${test_tagname_4}
    Page Should Contain  ${test_tagname_5}

Delete Last Tag From The List
    Go To Home Page
    Click Link  Hallinnoi tageja
    Click Element  xpath://*[@id="${test_tagname_5}"]
    Page Should Not Contain  ${test_tagname_5} 
    Page Should Contain  ${test_tagname_3}
    Page Should Contain  ${test_tagname_4} 

Delete All Remaining Tags From The List
    Go To Home Page
    Click Link  Hallinnoi tageja
    Click Element  xpath://*[@id="${test_tagname_3}"]
    Click Element  xpath://*[@id="${test_tagname_4}"]
    Page Should Not Contain  ${test_tagname}
    Page Should Not Contain  ${test_tagname_3}
    Page Should Not Contain  ${test_tagname_4}
    Page Should Not Contain  ${test_tagname_5}
