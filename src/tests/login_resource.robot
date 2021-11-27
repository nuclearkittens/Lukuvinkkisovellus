*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}
    
Set Password Confirm
    [Arguments]  ${password_confirm}
    Input Password  password_confirm  ${password_confirm}

Submit Login Credentials
    Click Button  Login
    
Submit Register Credentials
    Click Button  Sign up
    
Login Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
    
Register Should Fail With Message
    [Arguments]  ${message}
    Page Should Contain  ${message}
