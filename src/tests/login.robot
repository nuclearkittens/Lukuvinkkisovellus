*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***

Login With Nonexistent user
    Set Username  olematon
    Set Password  kayttaja
    Submit Login Credentials
    Login Should Fail With Message  Invalid username of password
