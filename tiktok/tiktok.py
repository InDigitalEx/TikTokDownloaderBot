from .content import Content


class TikTok:
    def __init__(self, link: str) -> None:
        self._content_maker = Content(link)

    @property
    def get_content(self) -> Content:
        return self._content_maker
