from tests.ui.conftest import setting_page


class TestSettingsPage:


    def test_add_child_folder(self, setting_page, inbox_page):
        setting_page.open()
        setting_page.create_folder("main")
        inbox_page.open()
        folder_element = inbox_page.folder_list.get_custom_folder("main")
        folder_element.is_visible()