*** Settings ***
Library  SeleniumLibrary
Library  PostgreSQLDB
Library  psycopg2
Library  ../AppLibrary.py
Library  DateTime

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}

#Tietokanta muuttujat
# Vaihda vastaamaan käytettävää tietokantaa
${dbname}  lukuvinkki
${dbuser}  tino
${dbpasswd}  ""
${script_file}  ./src/tests/robot_db_test.sql

#Testauksessa käytettäviä muuttujia.
#Login ja Register testi
${test_user_1}  Felix
${test_user_2}  Gotrek
${test_passwd_1}  Felix123
${test_passwd_2}  Gotrek123

#Kirja
${test_author}  Carlo Rovelli
${test_title}  Ajan luonne
${test_isbn}  978-952-5985-60-3
${test_description}  Ajan luonne purkaa ajan vyyhtiä fysiikan, filosofian ja taiteen avulla.
${test_author_2}  William King
${test_title_2}  Gotrek & Felix
${test_title_3}  Linnunrata
${test_isbn_3}  978-951-0-21844-0

#Blogi
${test_blog_writer}  Teemu Öhman
${test_blog_title}  Kraaterin reunalta
${test_blog_title_2}  Olutpostin olutblogit
${test_blog_url}  https://www.ursa.fi/blogi/kraatterin-reunalta.html
${test_blog_url2}  https://olutposti.fi/olutblogit/
${test_blog_description}  Planeettageologi ja kraatteritutkija Teemu Öhman käsittelee teksteissään aurinkokunnan kiinteäpintaisia kappaleita kokoon ja määritelmään katsomatta.

#Video
${test_video_title}  Hard Kokki: Opiskelijan kanakeitto
${test_video_title_2}  Hard Kokki: Makaronilaatikko
${test_video_url}  https://www.youtube.com/watch?v=PAa1KVqX9lk
${test_video_url_2}  https://www.youtube.com/watch?v=_2uVLtjAtQw
${test_video_description}  Vihdoin aivan saatanan halpaa ruokaa joka sopii persereikä aukisille ja opiskelijoille varsin hyvin.
${test_video_title_3}  INSOMNIUM - While We Sleep (OFFICIAL VIDEO)
${test_video_url_3}  https://www.youtube.com/watch?v=vBZ5SLJmfdw

#Podcast
${test_episode}  Jakso 7: Testaajan rooli ohjelmistokehityksessä
${test_episode_2}  Jakso 3: Alan opiskelu korkeakouluissa
${test_podcast_title}  Koodikahvit
${test_podcast_description}  Miten varmistetaan, että softa toimii kuten sen oletetaan toimivan?

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    #Maximize Browser Window
    Set Window Size  ${1920}  ${1080}
    Set Selenium Speed  ${DELAY}

Clear Database
    PostgreSQLDB.Connect To postgresql  ${dbname}  ${dbuser}  ${dbpasswd}
    ${output}=  PostgreSQLDB.Execute Plpgsql Script  ${script_file}
    log to console  ${output}
    Should Be Equal As Strings  ${output}  None
    PostgreSQLDB.Close All postgresql Connections    

Home Page Should Be Open
    Title Should Be  Lukuvinkkisovellus

Register Page Should Be Open
    Page Should Contain Button  Sign up

Go To Home Page
    Go To  ${HOME URL}

