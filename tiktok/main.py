from .fetcher import Fetcher


class TikTok:
    def __init__(self):
        self._content = []

    async def get_content_from_shared_link(self, shared_link: str):
        await self.__create_content_list_from_json(shared_link)
        return self._content

    async def __create_content_list_from_json(self, shared_link: str):
        fetcher = Fetcher(shared_link)
        data = await fetcher.fetch_api_json_data()
        self._content.append(data)
