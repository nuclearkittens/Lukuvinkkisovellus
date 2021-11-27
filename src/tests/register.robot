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
    
