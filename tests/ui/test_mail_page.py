class TestMailPage:

    def test_goto_drafts(self, inbox_page, drafts_page):
        inbox_page.open()
        inbox_page.folder_list.drafts.click()
        drafts_page.verify_url()

    def test_goto_sent(self, inbox_page, sent_page):
        inbox_page.open()
        inbox_page.folder_list.sent.click()
        sent_page.verify_url()

    def test_open_contact(self, inbox_page, contact_page):
        inbox_page.open()
        inbox_page.layout_menu.contacts_button.click()
        contact_page.verify_url()

    def test_open_settings(self, inbox_page, setting_page):
        inbox_page.open()
        inbox_page.layout_menu.settings_button.click()
        setting_page.verify_url()
