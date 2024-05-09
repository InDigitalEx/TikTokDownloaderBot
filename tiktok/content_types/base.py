from typing import Union


class MediaObject(object):
    def __init__(self, media: Union[str, list]) -> None:
        self._media = media

    @property
    def media(self) -> Union[str, list]:
        return self._media
