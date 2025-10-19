from pages.base_page import BasePage


class ContactsPage(BasePage):
    def __init__(self, page):
        super().__init__(page, "/", query_params={
            "_task" : "addressbook",
            "_source" : "0",
            "_gid": ""
        })