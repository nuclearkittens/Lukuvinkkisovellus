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
${test_author_2_edit}  Nathan Long
${test_title_2}  Gotrek & Felix
${test_title_2_edit}  Gotrek & Felix: Man Slayer
${test_isbn_2_edit}  978-1844165094
${test_description_2_edit}  Now back in the Empire following their sojourn overseas, Gotrek and Felix head north, to aid the men of the Empire in their fight against the invading Chaos hordes.
${test_title_3}  Linnunrata
${test_isbn_3}  978-951-0-21844-0

#Blogi
${test_blog_writer}  Teemu Öhman
${test_blog_writer_3}  Humalablogisti
${test_blog_title}  Kraaterin reunalta
${test_blog_title_2}  Olutpostin olutblogit
${test_blog_title_3}  Humalablogi
${test_blog_url}  https://www.ursa.fi/blogi/kraatterin-reunalta.html
${test_blog_url_2}  https://olutposti.fi/olutblogit/
${test_blog_url_3}  http://humalablogi.info/
${test_blog_description}  Planeettageologi ja kraatteritutkija Teemu Öhman käsittelee teksteissään aurinkokunnan kiinteäpintaisia kappaleita kokoon ja määritelmään katsomatta.
${test_blog_description_3}  Blogi olutmetsästyksen maailmaan. 

#Video
${test_video_title}  Hard Kokki: Opiskelijan kanakeitto
${test_video_title_2}  Hard Kokki: Makaronilaatikko
${test_video_url}  https://www.youtube.com/watch?v=PAa1KVqX9lk
${test_video_url_2}  https://www.youtube.com/watch?v=_2uVLtjAtQw
${test_video_description}  Vihdoin aivan saatanan halpaa ruokaa joka sopii persereikä aukisille ja opiskelijoille varsin hyvin.
${test_video_title_3_edit}  INSOMNIUM - While We Sleep
${test_video_title_3}  INSOMNIUM - While We Sleep (OFFICIAL VIDEO)
${test_video_url_3}  https://www.youtube.com/watch?v=vBZ5SLJmfdw
${test_video_description_3}  Hyvä kappale Insomniumilta.

#Podcast
${test_episode}  Jakso 7: Testaajan rooli ohjelmistokehityksessä
${test_episode_2}  Jakso 3: Alan opiskelu korkeakouluissa
${test_episode_3}  Jatkuva koodarina kehittyminen
${test_podcast_title}  Koodikahvit
${test_podcast_title_3}  Koodikahvit jakso 2
${test_podcast_description}  Miten varmistetaan, että softa toimii kuten sen oletetaan toimivan?
${test_podcast_description_3}  Koodikahvien kolmas jakso jatkaa edellisen jakson aiheesta eli koodaustaitojen kehittämisestä.

#Tagi
${test_tagname}  opiskelu
${test_tagname_2}  ab
${test_tagname_3}  matematiikka
${test_tagname_4}  jännitys
${test_tagname_5}  kauhu

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

