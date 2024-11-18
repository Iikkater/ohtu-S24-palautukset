*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  miikka
    Set Password  password123
    Set Password Confirmation  password123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  a
    Set Password  asdasd123
    Set Password Confirmation  asdasd123
    Submit Registration
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  asd
    Set Password  a
    Set Password Confirmation  a
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  qwe
    Set Password  qweqweqwe
    Set Password Confirmation  qweqweqwe
    Submit Registration
    Registration Should Fail With Message  Password must contain at least one non-letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  zxc
    Set Password  zxczxc123
    Set Password Confirmation  asdasd123
    Submit Registration
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  iikka
    Set Password  salasana123
    Set Password Confirmation  salasana123
    Submit Registration
    Registration Should Fail With Message  Username is already in use

*** Keywords ***

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  iikka  salasana123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}