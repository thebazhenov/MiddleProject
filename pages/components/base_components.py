from playwright.sync_api import expect, Locator

class BaseComponents:
    def __init__(self, locator: Locator):
        self._expect = expect
        self.locator = locator

    @property
    def expect(self):
        return self._expect

    def is_visible(self):
        return self.locator.is_visible()
