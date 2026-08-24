import os

import allure
import pytest
from data.test_data_registration import (
    REGISTRATION_TEST_DATA,
    PARTIAL_TEST_DATA,
    INVALID_MOBILE_DATA,
    RegistrationData,
    PartialRegistrationData
)


@allure.feature("Registration Form")
class TestRegistrationForm:

    @allure.story("Positive tests")
    @allure.title("Заполнение формы валидными данными")
    @pytest.mark.positive
    @pytest.mark.parametrize("data", REGISTRATION_TEST_DATA, ids=["maria_ivanova", "ivan_ivanov"])
    def test_fill_form_positive(self, registration_page, data: RegistrationData):
        with allure.step(f"Заполнить форму данными пользователя {data.first_name} {data.last_name}"):
            registration_page.fill_form(data)
        with allure.step("Нажать Submit"):
            registration_page.click_submit_button()
        with allure.step("Проверить результат"):
            result = registration_page.get_result_form()
            assert data.first_name in result
            assert data.last_name in result
            assert data.email in result
            assert data.mobile in result
            assert data.current_address in result
            assert data.state in result
            assert data.city in result

        if os.path.exists("test_image.jpg"):
            os.remove("test_image.jpg")

    @allure.story("Negative tests")
    @allure.title("Отправка пустой формы")
    @pytest.mark.negative
    def test_negative_empty_form(self, registration_page):
        with allure.step("Закрыть баннер"):
            registration_page.close_banner()
        with allure.step("Нажать Submit без заполнения"):
            registration_page.click_submit_button()
        with allure.step("Проверить сообщение об ошибке"):
            assert registration_page.get_error_message() == "Please fill required fields and enter a valid 10-digit mobile number."

    @allure.story("Negative tests")
    @allure.title("Проверка обязательных полей")
    @pytest.mark.negative
    @pytest.mark.parametrize("test_data", PARTIAL_TEST_DATA,
                             ids=["missing_first_name", "missing_last_name", "missing_gender", "missing_mobile"])
    def test_required_fields(self, registration_page, test_data: PartialRegistrationData):
        with allure.step("Заполнить форму с пропущенным полем"):
            registration_page.fill_form_partial(test_data)
        with allure.step("Нажать Submit"):
            registration_page.scroll_to_submit()
            registration_page.click_submit_button()
        with allure.step("Проверить сообщение об ошибке"):
            error = registration_page.get_error_message()
            assert "Please fill required fields and enter a valid 10-digit mobile number." in error

    @allure.story("Negative tests")
    @allure.title("Невалидный номер телефона: {test_data.mobile}")
    @pytest.mark.negative
    @pytest.mark.parametrize("test_data", INVALID_MOBILE_DATA,
                             ids=["too_short_3", "too_short_9", "too_long_11", "letters", "with_dashes"])
    def test_invalid_mobile(self, registration_page, test_data: PartialRegistrationData):
        with allure.step(f"Заполнить форму с телефоном '{test_data.mobile}'"):
            registration_page.fill_form_partial(test_data)
        with allure.step("Нажать Submit"):
            registration_page.scroll_to_submit()
            registration_page.click_submit_button()
        with allure.step("Проверить сообщение об ошибке"):
            error = registration_page.get_error_message()
            assert "Please fill required fields and enter a valid 10-digit mobile number." in error
