from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page, "/", query_params={
            "_task" : "mail",
            "_mbox" : "INBOX"
        })

