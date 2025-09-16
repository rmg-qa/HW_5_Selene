import os
from selene import browser, be, have


def test_send_form(browser_settings):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[placeholder="First Name"]').type('Роман').should(have.value('Роман'))  # First Name + assert
    browser.element('[placeholder="Last Name"]').type('Гороховик').should(have.value('Гороховик'))  # Last Name + assert
    browser.element('[id="userEmail"]').type('roman_qa@gmail.com').should(have.value('roman_qa@gmail.com'))  # Email + aseert
    browser.element('[for="gender-radio-1"]').click().should(be.clickable)  # Gender. Проверку можно выполнить только через execute_script. Фронт никак не отображает в DOM активное св-во этого элемента. Сделал проверку на кликабельность.
    browser.element('[id="userNumber"]').type('9963334558').should(have.value('9963334558'))  # Phone + assert
    browser.element('[id="dateOfBirthInput"]').click()  #Datapicker
    browser.element('[class="react-datepicker__month-select"]').click()  #Datapicker
    browser.element('.//option[@value="9"]').click()  #Datapicker
    browser.element('[class="react-datepicker__year-select"]').click()  #Datapicker
    browser.element('[value="1996"]').click()  #Datapicker
    browser.element('[class="react-datepicker__day react-datepicker__day--001"]').click()  #Datapicker
    browser.element('[id="dateOfBirthInput"]').should(have.value('01 Oct 1996'))  #assert Datapicker
    browser.element('[id="subjectsInput"]').type('math')  #Subjects
    browser.element('[id="react-select-2-option-0"]').click()  #Subjects
    browser.element(".//div[contains(@class, 'multiValue')]//child::div[1]").should(have.text('Maths'))  #assert Subjects
    browser.element('[for="hobbies-checkbox-1"]').click().should(be.clickable)  # Hobbies. Проверку можно выполнить только через execute_script. Фронт никак не отображает в DOM активное св-во этого элемента. Сделал проверку на кликабельность.
    browser.element('.//input[@class="form-control-file"]').type(os.path.abspath('qa-guru.jpg'))  # Picture. Проверку можно выполнить только через execute_script. Фронт никак не отображает в DOM активное св-во этого элемента
    browser.element('[id="currentAddress"]').type('Кемерово, ул. Советсткая, д.6').should(have.value('Кемерово, ул. Советсткая, д.6'))  #Current Address + assert
    browser.element('[id="state"]').click()  #State
    browser.element('[id="react-select-3-option-0"]').click()  #State
    browser.element('[id="state"]').should(have.text('NCR'))  #assert State
    browser.element('[id="city"]').click()  #City
    browser.element('[id="react-select-4-option-0"]').click()  #City
    browser.element('[id="city"]').should(have.text('Delhi'))  #assert City
    browser.element('[id="submit"]').click()  # Button "Submit"
    browser.element('[class="modal-title h4"]').should(have.text('Thanks for submitting the form'))  #Assert test is correct