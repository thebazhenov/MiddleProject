

class TestMainPage:

    def test_open_contact(self, main_page, contact_page):
        main_page.goto()
        main_page.verify_url()
        main_page.page_components.contacts_button.click(timeout=20000)
        contact_page.verify_url()