*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***

Login With Nonexistent user
    Set Username  olematon
    Set Password  Felix123
    Submit Login Credentials
    Login Should Return Message  Invalid username of password

Login With Wrong Password
    Set Username  ${test_user_1}
    Set Password  Felix213
    Submit Login Credentials
    Login Should Return Message  Invalid username of password

Login With Correct Credentials
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_1}
    Submit Login Credentials
    Login Should Return Message  login succesful

Logout From Application
    Click Link   xpath=//*[@id="logout"]
    Login Should Return Message  logged out
