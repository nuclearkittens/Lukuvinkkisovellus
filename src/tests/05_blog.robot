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
    Set Writer  ${test_blog_writer}
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

Blog Is Found From List
    Go To Home Page
    Page Should Contain  ${test_blog_title}
    
Blog Is Not Marked As Read
    Element Should Contain  //*[@id="${test_blog_title}_"]  Luettu: None

Mark Blog As Read
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_blog_title}"]
    Click Element  xpath://*[@name="read_check"]/following-sibling::label[@id="mark_read"]
    Click Button  Muokkaa
    ${time_now}=  Get Current Date  result_format=%Y-%m-%d %H:%M
    Element Should Contain  //*[@id="${test_blog_title}_"]  ${time_now}

Mark Blog As Unread
    Press Keys  None  PAGE_DOWN
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_blog_title}"]
    Click Element  xpath://*[@name="read_check"]/following-sibling::label[@id="mark_unread"]
    Click Button  Muokkaa
    Element Should Contain  //*[@id="${test_blog_title}_"]  Luettu: None

Edit Blog
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_blog_title_2}"]
    Set Writer  ${test_blog_writer_3}
    Set Blogtitle  ${test_blog_title_3}
    Set Url  ${test_blog_url_3}
    Set Description  ${test_blog_description_3}
    Click Button  Muokkaa
    Page Should Contain  ${test_blog_title_3}
    Page Should Contain  ${test_blog_writer_3}
    Page Should Contain  ${test_blog_description_3}

Delete Blog
    Press Keys  None  PAGE_DOWN
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_blog_title_}"]
    Click Button  Poista lukuvinkki
    Sleep  1
    Click Button  Kyllä, poista
    Page Should Not Contain  Tähdellä (*) merkityt kohdat ovat pakollisia
    Page Should Not Contain  ${test__blog_title}
    #Joudun luomaan uuden blogin, koska muuten filter testit kusee.
    Click Link  xpath://a[@href="/new_blog"]
    Set Writer  ${test_blog_writer}
    Set Blogtitle  ${test_blog_title}
    Set Url  ${test_blog_url}
    Set Description  ${test_blog_description}
    Click Element  submit
