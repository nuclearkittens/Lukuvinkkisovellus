*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Opens
    Home Page Should Be Open

Click Register Link
    Click Link  Click here to register!
    Register Page Should Be Open
