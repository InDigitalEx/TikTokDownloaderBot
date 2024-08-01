from aiohttp import ClientSession


class Fetcher(object):
    def __init__(self, link: str = None) -> None:
        self._basic_url = 'https://ssstik.io'
        self._url = '/abc?url=dl'
        self._data = f'id={link}&locale=en&tt=YXpMTE1l'
        self._headers = {
            'accept'                     : '*/*',
            'accept-language'            : 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,bg;q=0.6',
            'content-type'               : 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie'                     : '_ga=GA1.1.345600929.1715042357; _ga_ZSF3D6YSLC=GS1.1.1715200059.4.1.1715200378.0.0.0',
            'hx-current-url'             : 'https://ssstik.io/',
            'hx-request'                 : 'true',
            'hx-target'                  : 'target',
            'hx-trigger'                 : '_gcaptcha_pt',
            'origin'                     : 'https://ssstik.io',
            'priority'                   : 'u=1, i',
            'referer'                    : 'https://ssstik.io/',
            'sec-ch-ua'                  : '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-arch'             : '"x86"',
            'sec-ch-ua-bitness'          : '"64"',
            'sec-ch-ua-full-version'     : '"124.0.6367.118"',
            'sec-ch-ua-full-version-list': '"Chromium";v="124.0.6367.118", "Google Chrome";v="124.0.6367.118", "Not-A.Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile'           : '?0',
            'sec-ch-ua-model'            : '""',
            'sec-ch-ua-platform'         : '"Linux"',
            'sec-ch-ua-platform-version' : '"6.2.0"',
            'sec-fetch-dest'             : 'empty',
            'sec-fetch-mode'             : 'cors',
            'sec-fetch-site'             : 'same-origin',
            'user-agent'                 : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        }

    async def fetch_data(self):
        async with ClientSession(self._basic_url) as session:
            async with session.post(self._url, data=self._data, headers=self._headers) as response:
                return await response.text()

    @property
    def headers(self):
        return self._headers
