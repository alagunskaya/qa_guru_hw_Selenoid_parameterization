from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def find_element(self, locator):
        """Находит элемент с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Кликает по элементу"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        """Вводит текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Получает текст элемента"""
        return self.find_element(locator).text

    def is_visible(self, locator):
        """Проверяет видимость элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def wait_for_visible(self, locator):
        """Ожидает появления элемента"""
        self.wait.until(EC.visibility_of_element_located(locator))

    def upload_file(self, locator, file_path: str):
        """Найти инпут загрузки файла и передать путь"""
        element = self.find_element(locator)
        element.send_keys(file_path)
