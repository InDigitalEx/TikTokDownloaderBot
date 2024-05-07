from typing import Final, Any

from aiohttp import ClientSession

from .exceptions import FetcherError


class Fetcher:
    """
    Fetch json information about a video from a TikTok shared link
    """
    _API_URL: Final = (
        'https://api22-normal-c-alisg.tiktokv.com/aweme/v1/feed/?aweme_id={content_id}'
        '&iid=7318518857994389254&device_id=7318517321748022790&channel=googleplay&app_name'
        '=musical_ly&version_code=300904&device_platform=android&device_type=ASUS_Z01QD&version=9'
    )
    _HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/75.0.3770.100 Safari/537.36'
    }

    def __init__(self, shared_link: str) -> None:
        """
        Initializes an instance of a class
        @param shared_link: Link like https://**.tiktok.com/*/*
        """
        self._shared_link = shared_link
        self._is_video = None

    async def fetch_api_json_data(self) -> Any:
        """
        Fetch data from a link like https://**.tiktok.com/*/*
        @return: Json data received from api
        """
        async with ClientSession() as session:
            redirect_url = await self.__get_redirect_url(self._shared_link, session)
            content_id = self.__get_content_id_by_redirect_url(redirect_url)

            try:
                async with session.get(
                        self._API_URL.format(content_id=content_id),
                        headers=self._HEADERS
                ) as response:
                    data = []
                    if self.is_video:
                        data = (await response.json())['aweme_list'][0]['video']['play_addr']['url_list'][0]
                    if self.is_photos:
                        raise FetcherError("Photos are not available at the moment")
                    return data
            except Exception:
                raise FetcherError("An error occurred while retrieving TikTok API data")

    @property
    def is_video(self):
        return self._is_video

    @property
    def is_photos(self):
        return not self._is_video
    
    async def __get_redirect_url(self, shared_link: str, session: ClientSession):
        """
        Make a redirect to get a link to the TikTok content
        @param shared_link: Link like https://**.tiktok.com/*/*
        @param session: aiohttp client session
        @return: link to TikTok content
        """
        try:
            async with session.get(shared_link, allow_redirects=False, headers=self._HEADERS) as response:
                return response.headers.get('location')
        except Exception:
            raise FetcherError("An error occurred while retrieving the redirect url")

    def __get_content_id_by_redirect_url(self, redirect_url: str) -> str:
        """
        Get the content ID from the specified link
        @param redirect_url: Content redirect link
        @return: Content id
        """
        if 'video' in redirect_url:
            self._is_video = True
        if 'photo' in redirect_url:
            self._is_video = False
        try:
            parts = redirect_url.split('/')
            content_id = parts[-1].split('?')[0]
            return content_id
        except Exception:
            raise FetcherError("Unable to get content id")
