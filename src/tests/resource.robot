*** Settings ***
Library  SeleniumLibrary
Library  PostgreSQLDB
Library  psycopg2
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.2 seconds
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


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
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
