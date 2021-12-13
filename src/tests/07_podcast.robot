*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Resource  data_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

 
*** Test Cases ***
Add New Podcast Without Episode
    Set Username  ${test_user_1}
    Set Password  ${test_passwd_1}
    Submit Login Credentials    
    Click Link  xpath://a[@href="/new_podcast"]
    Set Podcasttitle  ${test_podcast_title}
    Set Description  ${test_podcast_description}
    Click Element  submit
    Page Should Contain  Tähdellä (*) merkityt kohdat ovat pakollisia

Add New Podcast Without Podcast Title
    Go To Home Page
    Click Link  xpath://a[@href="/new_podcast"]
    Set Episode  ${test_episode}
    Set Description  ${test_podcast_description}
    Click Element  submit
    Page Should Contain  Tähdellä (*) merkityt kohdat ovat pakollisia

Add New Podcast
    Go To Home Page
    Click Link  xpath://a[@href="/new_podcast"]
    Set Episode  ${test_episode}
    Set Podcasttitle  ${test_podcast_title}
    Set Description  ${test_podcast_description}
    Click Element  submit
    Page Should Contain  Lukuvinkkilista

Add podcast Without Description
    Go To Home Page
    Click Link  xpath://a[@href="/new_podcast"]
    Set Episode  ${test_episode_2}
    Set Podcasttitle  ${test_podcast_title}
    Click Element  submit
    Page Should Contain  Lukuvinkkilista
    
Podcast Is Found From List
    Go To Home Page
    Page Should Contain  ${test_podcast_title}
    
Podcast Is Not Marked As Read
    Element Should Contain  //*[@id="${test_episode}_"]  Luettu: None

Mark Podcast As Read
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_episode}"]
    Click Element  xpath://*[@name="read_check"]/following-sibling::label[@id="mark_read"]
    Click Button  Muokkaa
    ${time_now}=  Get Current Date  result_format=%Y-%m-%d %H:%M
    Element Should Contain  //*[@id="${test_episode}_"]  ${time_now}

Mark Podcast As Unread
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_episode}"]
    Click Element  xpath://*[@name="read_check"]/following-sibling::label[@id="mark_unread"]
    Click Button  Muokkaa
    Element Should Contain  //*[@id="${test_episode}_"]  Luettu: None
    
Edit Podcast
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_episode_2}"]
    Set Episode  ${test_episode_3}
    Set Podcasttitle  ${test_podcast_title_3}
    Set Description  ${test_podcast_description_3}
    Click Button  Muokkaa
    Page Should Contain  ${test_episode_3}
    Page Should Contain  ${test_podcast_title_3}
    Page Should Contain  ${test_podcast_description_3}

Delete Podcast
    Press Keys  None  PAGE_DOWN
    Sleep  1
    Click Element  xpath://*[@id="${test_episode}"]
    Click Button  Poista lukuvinkki
    Sleep  1
    Click Button  Kyllä, poista
    Page Should Not Contain  Tähdellä (*) merkityt kohdat ovat pakollisia
    Page Should Not Contain  ${test_episode}
    #Joudun luomaan uuden podcastin, koska muuten filter testit kusee
    Click Link  xpath://a[@href="/new_podcast"]
    Set Episode  ${test_episode}
    Set Podcasttitle  ${test_podcast_title}
    Set Description  ${test_podcast_description}
    Click Element  submit
