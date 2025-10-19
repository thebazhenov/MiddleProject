from context.page_context import PageContext
from pages.elements.href import Href


class FolderListComponents:
    def __init__(self, page: PageContext):
        self.page = page

    @property
    def drafts(self):
        return Href(self.page.get_by_role("link", name=" Черновики"))

    @property
    def sent(self):
        return Href(self.page.get_by_role("link", name=" Отправленные"))

    @property
    def inbox(self):
        return Href(self.page.get_by_role("link", name=" Входящие"))

    def get_custom_folder(self, name_folder: str):
        return Href(self.page.get_by_role("link", name=f" {name_folder}", exact=True))


