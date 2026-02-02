*** Settings ***
Library    OperatingSystem

*** Test Cases ***
Check Images Folder Exists
    Directory Should Exist    Images

Check Docs Folder Exists
    Directory Should Exist    Docs