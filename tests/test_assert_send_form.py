import os
from selene import browser, have


def test_send_form(browser_settings):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[placeholder="First Name"]').type('Роман')  # First Name
    browser.element('[placeholder="Last Name"]').type('Гороховик')  # Last Name
    browser.element('[id="userEmail"]').type('roman_qa@gmail.com')  # Email
    browser.element('[for="gender-radio-1"]').click()  # Gender
    browser.element('[id="userNumber"]').type('9963334558')  # Phone
    browser.element('[id="dateOfBirthInput"]').click()  #Datapicker
    browser.element('[class="react-datepicker__month-select"]').click()  #Datapicker
    browser.element('.//option[@value="9"]').click()  #Datapicker
    browser.element('[class="react-datepicker__year-select"]').click()  #Datapicker
    browser.element('[value="1996"]').click()  #Datapicker
    browser.element('[class="react-datepicker__day react-datepicker__day--001"]').click()  #Datapicker
    browser.element('[id="subjectsInput"]').type('math')  #Subjects
    browser.element('.//div[@id="react-select-2-option-0"]').click()  #Subjects
    browser.element(".//div[contains(@class, 'multiValue')]//child::div[1]")
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('.//input[@class="form-control-file"]').type(os.path.abspath('qa-guru.jpg'))  # Picture.
    browser.element('[id="currentAddress"]').type('Кемерово, ул. Советсткая, д.6')
    browser.element('[id="state"]').click()  #State
    browser.element('[id="react-select-3-option-0"]').click()  #State
    browser.element('[id="city"]').click()  #City
    browser.element('[id="react-select-4-option-0"]').click()  #City
    browser.element('[id="submit"]').click()  # Button "Submit"
    browser.element('[class="modal-title h4"]').should(have.text('Thanks for submitting the form'))  #Assert test is correct
    browser.all("tbody").should(have.texts('Student Name Роман Гороховик\nStudent Email roman_qa@gmail.com\nGender Male\nMobile 9963334558\nDate of Birth 01 October,1996\nSubjects Maths\nHobbies Sports\nPicture qa-guru.jpg\nAddress Кемерово, ул. Советсткая, д.6\nState and City NCR Delhi'))