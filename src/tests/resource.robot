*** Settings ***
Library  SeleniumLibrary
Library  PostgreSQLDB
Library  psycopg2
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}
${dbname}  lukuvinkki
${dbuser}  postgresql


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Database Connection
    PostgreSQLDB.Connect To postgresql  ${dbname}  ${dbuser}  None
    Execute Sql String  select * from users
    PostgreSQLDB.Close All postgresql Connections

Home Page Should Be Open
    Title Should Be  Lukuvinkkisovellus

Register Page Should Be Open
    Page Should Contain Button  Sign up

Go To Home Page
    Go To  ${HOME URL}
