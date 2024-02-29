*** Settings ***
Documentation  Business facing UI dashboard tests in the language of the problem domain
Resource    ../../Resources/UI/selenium/CustomKeywords.robot
Test Teardown    Close Browser
*** Variables ***

*** Test Cases ***
As a user I can view the dashboard with loaded data
    [Documentation]    Data loads in table

    Given I am a user who is viewing the dashboard
    When the dashboard loads
    Then there is data loaded in the dashboard

# As a user I can clearly see a successful result
#     [Documentation]    Success shows as green

#     Given I am a user who is viewing the dashboard
#     When the dashboard loads
#     Then a successful result shows as green

# As a user I can clearly see a successful result
#     [Documentation]    Success shows as red

#     Given I am a user who is viewing the dashboard
#     When the dashboard loads
#     Then a successful result shows as red