from bs4 import BeautifulSoup

from .base import MediaObject


class Audio(MediaObject):
    def __init__(self, data: str):
        scraper = BeautifulSoup(data, 'html.parser')
        media = scraper.find('a', href=True, class_='music')

        super().__init__(media['href'])
