*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  data_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page


*** Test Cases ***

Add New Blog Without Title
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_1}
    Submit Login Credentials    
    Click Link  xpath://a[@href="/new_blog"]
    Set Writer  ${test_blog_title}
    Set Url  ${test_blog_url}
    Set Description  ${test_blog_description}
    Click Element  submit
    Page Should Contain  Tähdellä (*) merkityt kohdat ovat pakollisia

Add New Blog Without Url
    Go To Home Page
    Click Link  xpath://a[@href="/new_blog"]
    Set Writer  ${test_blog_writer}
    Set Blogtitle  ${test_blog_title}
    Set Description  ${test_blog_description}
    Click Element  submit
    Page Should Contain  Tähdellä (*) merkityt kohdat ovat pakollisia
    
Add New Blog Into List
    Go To Home Page
    Click Link  xpath://a[@href="/new_blog"]
    Set Writer  ${test_blog_writer}
    Set Blogtitle  ${test_blog_title}
    Set Url  ${test_blog_url}
    Set Description  ${test_blog_description}
    Click Element  submit
    Page Should Not Contain  Tähdellä (*) merkityt kohdat ovat pakollisia
    
Add New Blog Without Writer And Description
    Go To Home Page
    Click Link  xpath://a[@href="/new_blog"]
    Set Blogtitle  ${test_blog_title_2}
    Set Url  ${test_blog_url_2}
    Click Element  submit
    Page Should Not Contain  Tähdellä (*) merkityt kohdat ovat pakollisia
