from pages.mail_pages.main_page import MainPage


class InboxPage(MainPage):
    def __init__(self, page):
        super().__init__(page, "/", query_params={
            "_task" : "mail",
            "_mbox" : "INBOX"
        })
