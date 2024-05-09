from typing import Union

from bs4 import BeautifulSoup

from .audio import Audio
from .base import MediaObject


class MediaWithAudio(MediaObject):
    def __init__(self, content: Union[str, list], data: str):
        super().__init__(content)
        self._audio = Audio(data)

    @property
    def audio(self):
        return self._audio


class Video(MediaWithAudio):
    def __init__(self, data: str):
        scraper = BeautifulSoup(data, 'html.parser')

        media = scraper.find('a', href=True, class_='without_watermark')

        super().__init__(media['href'], data)


class Photos(MediaWithAudio):
    def __init__(self, data: str):
        scraper = BeautifulSoup(data, 'html.parser')

        photos_list = scraper.find('ul', class_='splide__list')
        hrefs = photos_list.find_all('a', href=True)
        media = [h['href'] for h in hrefs]

        super().__init__(media, data)
