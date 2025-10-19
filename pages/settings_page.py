import allure
from pages.base_page import BasePage
from pages.elements.button import Button
from pages.elements.iframe import Iframe

class SettingPage(BasePage):
    def __init__(self, page):
        super().__init__(page, "/", query_params={
            "_task" : "settings"
        })

    @property
    def folder_button(self):
        return Button(self.page.get_by_role("button", name=" Почта"))

    @property
    def create_folder_button(self):
        return Button(self.page.get_by_role("button", name=" Создать"))

    @property
    def create_folder_frame(self):
        return Iframe(self.locator("iframe[name=\"preferences-frame\"]").content_frame.get_by_role("textbox", name="Имя папки"))

    @allure.step("Создание папки")
    def create_folder(self, name_folder: str = "test"):
       self.folder_button.click()
       self.create_folder_button.click()
       self.create_folder_frame.click()
       self.create_folder_frame.fill(name_folder)
