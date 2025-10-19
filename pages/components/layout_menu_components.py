from context.page_context import PageContext
from pages.elements.button import Button


class LayoutMenuComponents:
    def __init__(self, page: PageContext):
        self.page = page

    @property
    def contacts_button(self):
        return Button(self.page.locator("#rcmbtn105"))

    @property
    def settings_button(self):
        return Button(self.page.get_by_role("button", name=" Настройки"))
