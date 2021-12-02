*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
    
Register With Too Short Username And Valid Password
    Click Link  Click here to register!
    Set Username  Yo
    Set Password  salasana
    Set Password Confirm  salasana
    Submit Register Credentials
    Register Page Should Be Open

Register With Too Short Password
    Click Link  Click here to register!
    Set Username  ${test_user_2}
    Set Password  abc
    Set Password Confirm  abc
    Submit Register Credentials
    Register Page Should Be Open
    
Register With Not matching Password And Confirmation
    Click Link  Click here to register!
    Set Username  ${test_user_2}
    Set Password  Gotrek123
    Set Password Confirm  gotrek123
    Submit Register Credentials
    Register Should Fail With Message  Field must be equal to password.
    
Register With Correct Credentials
    Click Link  Click here to register!
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_1}
    Set Password Confirm  ${test_passwd_1}
    Submit Register Credentials
    Register Should Succeed With Message  Registration succesful
    Click Link   xpath=//*[@id="logout"]

Register With Reserved Username
    Click Link  Click here to register!
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_2}
    Set Password Confirm  ${test_passwd_2}
    Submit Register Credentials
    Register Should Fail With Message  Username taken


