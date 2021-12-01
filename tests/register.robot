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
    Set Username  Gotrek
    Set Password  abc
    Set Password Confirm  abc
    Submit Register Credentials
    Register Page Should Be Open
    
Register With Not matching Password And Confirmation
    Click Link  Click here to register!
    Set Username  Gotrek
    Set Password  Gotrek123
    Set Password Confirm  gotrek123
    Submit Register Credentials
    Register Should Fail With Message  Field must be equal to password.

Register With Reserved Username
    Click Link  Click here to register!
    Set Username  Felix
    Set Password  123felix
    Set Password Confirm  123felix
    Submit Register Credentials
    Register Should Fail With Message  Username taken

Register With Correct Credentials
    Click Link  Click here to register!
    Set Username  Gotrek
    Set Password  Gotrek123
    Set Password Confirm  Gotrek123
    Submit Register Credentials
    Register Should Succeed With Message  Registration succesful
