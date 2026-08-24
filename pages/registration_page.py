import os
import time

import allure
from selenium.webdriver.support import expected_conditions as EC

from data.test_data_registration import RegistrationData, PartialRegistrationData
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPage(BasePage):
    PAGE_URL = "https://demo.qa.guru/one-page-form/automation-practice-form.html"

    FIRST_NAME = (By.CSS_SELECTOR, "#firstName")
    LAST_NAME = (By.CSS_SELECTOR, "#lastName")
    USER_EMAIL = (By.CSS_SELECTOR, "#userEmail")
    MOBILE_NUMBER = (By.CSS_SELECTOR, "#userNumber")
    DATE_INPUT = (By.CSS_SELECTOR, "#dateOfBirthInput")
    SUBJECTS_INPUT = (By.CSS_SELECTOR, "#subjectsInput")
    PICTURE_INPUT = (By.CSS_SELECTOR, "#uploadPicture")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "#currentAddress")
    CITY_INPUT = (By.CSS_SELECTOR, "#city")
    STATE_INPUT = (By.CSS_SELECTOR, "#state")
    CITY_DROP_DOWN = (By.CSS_SELECTOR, "#stateCity-wrapper")
    STATE_DROP_DOWN = (By.CSS_SELECTOR, "#stateCity-wrapper")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#submit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#formError")
    RESULT_BODY = (By.CSS_SELECTOR, "#resultBody")

    # Календарь
    DAY_OPTION = (By.CSS_SELECTOR,
                  "div.react-datepicker__day--0{padded_day}:not(.react-datepicker__day--outside-month)")
    YEAR_SELECT = (By.CSS_SELECTOR, "select[class='react-datepicker__year-select']")
    MONTH_SELECT = (By.CSS_SELECTOR, "select[class='react-datepicker__month-select']")
    CALENDAR = (By.CSS_SELECTOR, "div[class='react-datepicker__month-container']")

    @allure.step("Открыть страницу регистрации")
    def open(self):
        self.driver.get(self.PAGE_URL)

    @allure.step("Закрыть баннер")
    def close_banner(self):
        self.click_element((By.CSS_SELECTOR, "button[aria-label='Close']"))

    @allure.step("Ввести имя: {first_name}")
    def input_first_name(self, first_name: str):
        self.type_text(self.FIRST_NAME, first_name)

    @allure.step("Ввести фамилию: {last_name}")
    def input_last_name(self, last_name: str):
        self.type_text(self.LAST_NAME, last_name)

    @allure.step("Ввести email: {email}")
    def input_email(self, email: str):
        self.type_text(self.USER_EMAIL, email)

    @allure.step("Выбрать гендер: {gender}")
    def select_gender(self, gender: str):
        allowed_genders = ["Male", "Female", "Other"]
        if gender not in allowed_genders:
            raise ValueError(f"Недопустимый гендер: '{gender}'. Допустимо: {allowed_genders}")

        locator = (By.XPATH, f"//label[.//input[@type='radio' and @value='{gender}']]")
        self.click_element(locator)

    @allure.step("Ввести номер телефона: {mobile_number}")
    def input_mobile_number(self, mobile_number: str):
        self.type_text(self.MOBILE_NUMBER, mobile_number)

    @allure.step("Выбрать дату рождения: {day}.{month}.{year}")
    def select_date_of_birth(self, day: int, month: int, year: int):
        self.click_element(self.DATE_INPUT)
        self.wait_for_visible(self.CALENDAR)

        month_select = self.find_element(self.MONTH_SELECT)
        month_select.click()
        month_select.find_element(By.XPATH, f"//option[@value='{month - 1}']").click()

        year_select = self.find_element(self.YEAR_SELECT)
        year_select.click()
        year_select.find_element(By.XPATH, f"//option[@value='{year}']").click()

        day_locator = (By.XPATH,
                       f"//span[contains(@class, 'react-datepicker__day') and text()='{day}' and not(contains(@class, 'react-datepicker__day--outside-month'))]")
        self.click_element(day_locator)

    @allure.step("Ввести предметы: {subjects}")
    def input_subjects(self, subjects: list | str):
        subjects_list = subjects if isinstance(subjects, list) else [subjects]
        input_subject = self.find_element(self.SUBJECTS_INPUT)

        for subject in subjects_list:
            input_subject.send_keys(subject)
            # Ждем появления варианта в списке
            first_option = (By.XPATH,
                            f"//div[contains(@class, 'subjects-auto-complete__option') and text()='{subject}']")
            self.wait.until(EC.visibility_of_element_located(first_option))
            self.click_element(first_option)
        self.driver.execute_script("arguments[0].blur();", input_subject)

    @allure.step("Выбрать хобби: {hobbies}")
    def select_hobbies(self, hobbies: list | str):
        hobbies_list = hobbies if isinstance(hobbies, list) else [hobbies]

        for hobby in hobbies_list:
            hobby_normalized = hobby.strip().capitalize()

            locator = (By.XPATH, f"//label[contains(text(), '{hobby_normalized}')]")
            self.click_element(locator)

    @allure.step("Загрузить фото")
    def upload_picture(self, file_path: str = None):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        if file_path is None:
            temp_file_path = os.path.abspath("test_image.jpg")
            with open(temp_file_path, "w") as f:
                f.write("Image data")
            file_path = temp_file_path

        self.upload_file(self.PICTURE_INPUT, file_path)

    @allure.step("Выбрать штат: {state_name}")
    def select_state(self, state_name: str):
        self.click_element(self.STATE_INPUT)
        self.wait.until(EC.visibility_of_element_located(self.STATE_DROP_DOWN))

        state_option = (By.XPATH, f"//div[@class='state-city-option' and text()='{state_name}']")
        state = self.wait.until(EC.element_to_be_clickable(state_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state)
        self.driver.execute_script("arguments[0].click();", state)

    @allure.step("Выбрать город: {city_name}")
    def select_city(self, city_name: str):
        self.click_element(self.CITY_INPUT)
        self.wait.until(EC.visibility_of_element_located(self.CITY_DROP_DOWN))

        city_option = (By.XPATH, f"//div[@class='state-city-option' and text()='{city_name}']")
        city = self.wait.until(EC.element_to_be_clickable(city_option))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city)
        self.driver.execute_script("arguments[0].click();", city)

    @allure.step("Ввести текущий адрес: {current_address}")
    def input_current_address(self, current_address: str):
        element = self.find_element(self.CURRENT_ADDRESS)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.type_text(self.CURRENT_ADDRESS, current_address)

    @allure.step("Прокрутить до кнопки Submit")
    def scroll_to_submit(self):
        element = self.find_element(self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Нажать кнопку Submit")
    def click_submit_button(self):
        self.scroll_to_submit()
        time.sleep(2)
        self.click_element(self.SUBMIT_BUTTON)

    @allure.step("Получить результат отправки")
    def get_result_form(self) -> str:
        """Получить форму с результатом"""
        self.wait_for_visible(self.RESULT_BODY)
        return self.get_text(self.RESULT_BODY)

    @allure.step("Получить сообщение об ошибке")
    def get_error_message(self) -> str:
        """Получить текст ошибки"""
        self.wait_for_visible(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)

    @allure.step("Заполнить форму полностью")
    def fill_form(self, data: RegistrationData):
        self.close_banner()
        self.input_first_name(data.first_name)
        self.input_last_name(data.last_name)
        self.input_email(data.email)
        self.select_gender(data.gender)
        self.input_mobile_number(data.mobile)
        self.select_date_of_birth(data.day, data.month, data.year)
        self.input_subjects(data.subjects)
        self.select_hobbies(data.hobbies)
        self.upload_picture()
        self.input_current_address(data.current_address)
        self.select_state(data.state)
        self.select_city(data.city)

    @allure.step("Заполнить форму частично")
    def fill_form_partial(self, data: PartialRegistrationData):
        self.close_banner()

        if data.first_name:
            self.input_first_name(data.first_name)
        if data.last_name:
            self.input_last_name(data.last_name)
        if data.email:
            self.input_email(data.email)
        if data.gender:
            self.select_gender(data.gender)
        if data.mobile:
            self.input_mobile_number(data.mobile)
        if data.day and data.month and data.year:
            self.select_date_of_birth(data.day, data.month, data.year)
        if data.subjects:
            self.input_subjects(data.subjects)
        if data.hobbies:
            self.select_hobbies(data.hobbies)
        if data.current_address:
            self.input_current_address(data.current_address)
        if data.state:
            self.select_state(data.state)
        if data.city:
            self.select_city(data.city)
