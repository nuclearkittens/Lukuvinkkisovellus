*** Keywords ***
Set Booktitle
    [Arguments]  ${bookname}
    Input Text  title  ${bookname}

Set Writer
    [Arguments]  ${author}
    Input Text  author  ${author}

Set ISBN
    [Arguments]  ${isbn}
    Input Text  isbn  ${isbn}
    
Set Description
    [Arguments]  ${description}
    Input Text  description  ${description}
    
Adding Item Should Return Message
    [Arguments]  ${message}
    Page Should Contain  ${message}

Set Blogtitle
    [Arguments]  ${blogtitle}
    Input Text  title  ${blogtitle}

Set Videotitle
    [arguments]  ${videotitle}
    Input Text  title  ${videotitle}
    
Set Podcasttitle
    [arguments]  ${podcasttitle}
    Input Text  title  ${podcasttitle}
    
Set Episode
    [arguments]  ${episode}
    Input Text  episode  ${episode}
    
Set Url
    [Arguments]  ${url}
    Input Text  url  ${url}
    
