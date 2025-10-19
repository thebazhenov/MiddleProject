from pages.base_page import BasePage
from pages.elements.button import Button


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page, "/")  # Вызываем конструктор базового класса

    @property
    def login_field(self):
        return self.locator("#rcmloginuser")

    @property
    def password_field(self):
        return self.locator("#rcmloginpwd")

    @property
    def submit_button(self):
        return self.locator("#rcmloginsubmit")

    def login(self, username: str, password: str):
        self.login_field.fill(username)
        self.password_field.fill(password)
        Button(self.submit_button).verify_enabled()
        Button(self.submit_button).click()
