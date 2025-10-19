from pages.base_page import BasePage
from pages.mail_pages.components.folder_list_components import FolderListComponents


class MainPage(BasePage):
    def __init__(self, page, path: str, query_params: dict | None = None):
        super().__init__(page, path="/", query_params=query_params)

    @property
    def folder_list(self):
        return FolderListComponents(self.page)