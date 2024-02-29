*** Settings ***
Documentation  Custom keywords to abstract details from 
Library    SeleniumLibrary

*** Keywords ***
I am a user who is viewing the dashboard
    Open Browser  http://localhost:3000

the dashboard loads
    Wait Until Element Contains    id:orderTable    23404
    
there is data loaded in the dashboard
    Table Row Should Contain    id:orderTable    1    ✓