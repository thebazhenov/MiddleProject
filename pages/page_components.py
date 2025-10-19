from playwright.sync_api import Page, Locator, expect


class PageComponents:
    def __init__(self, page: Page):
        self.page = page

    @property
    def contacts_button(self):
        return Button(self.page.locator("#rcmbtn105"))


class Button:
    def __init__(self, locator: Locator):
        self.locator = locator

    def click(self, *args, **kwargs):
        return self.locator.click(*args, **kwargs)

    def verify_enabled(self, status: bool = True):
        if status:
            expect(self.locator).to_be_enabled()
        else:
            expect(self.locator).not_to_be_enabled()

