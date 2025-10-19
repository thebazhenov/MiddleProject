import time
import allure
from base_page import BasePage, PageContext


class LoginPage(BasePage):
    def __init__(self, page: PageContext):
        super().__init__(page)  # Вызываем конструктор базового класса
        self.login_field = "rcmloginuser"
        self.password_field = "rcmloginpwd"

    @allure.step("Write login")
    def write_login(self):
        self.page.type(selector=self.login_field, text="test@localhost.com")


