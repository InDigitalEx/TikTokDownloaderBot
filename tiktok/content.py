from enum import Enum
from typing import Optional, Union

from bs4 import BeautifulSoup

from .api import Fetcher
from .content_types import Video, Photos


class ContentType(Enum):
    NONE = 0
    VIDEO = 1
    PHOTOS = 2


class Content(object):
    def __init__(self, link: str):
        self._link: str = link
        self._data: Optional[str] = None
        self._content_type: ContentType = ContentType.NONE
        self._video: Optional[Video] = None
        self._photos: Optional[Photos] = None

    async def _fetch_data(self):
        fetcher = Fetcher(self._link)
        self._data = await fetcher.fetch_data()

    async def _detect_type_of_content(self) -> Union[None, Video, Photos]:
        if self._content_type == ContentType.VIDEO:
            return self._video
        elif self._content_type == ContentType.PHOTOS:
            return self._photos

        await self._fetch_data()
        scraper = BeautifulSoup(self._data, 'html.parser')

        if scraper.find('div', id='dl1'):
            self._content_type = ContentType.VIDEO
            self._video = Video(self._data)

            return self._video
        elif scraper.find('div', class_='splide'):
            self._content_type = ContentType.PHOTOS
            self._photos = Photos(self._data)

            return self._photos
        else:
            return None

    async def make_content(self) -> bool:
        return await self._detect_type_of_content() is not None

    @property
    async def content_type(self) -> ContentType:
        content = await self._detect_type_of_content()
        if content is None:
            return ContentType.NONE
        elif isinstance(content, Video):
            return ContentType.VIDEO
        elif isinstance(content, Photos):
            return ContentType.PHOTOS

    @property
    async def is_video(self) -> bool:
        return isinstance(await self._detect_type_of_content(), Video)

    @property
    async def is_photos(self) -> bool:
        return isinstance(await self._detect_type_of_content(), Photos)

    @property
    async def video(self) -> Optional[Video]:
        content = await self._detect_type_of_content()
        return content if isinstance(content, Video) else None

    @property
    async def photos(self) -> Optional[Photos]:
        content = await self._detect_type_of_content()
        return content if isinstance(content, Photos) else None

    @property
    async def content(self) -> Union[None, Video, Photos]:
        return await self._detect_type_of_content()
