import requests
from shorty.constants import TINY_URL_ACCESS_TOKEN

class TinyUrlClient:
    """
    Should have been abstracted
    Secrets in clear
    """

    base_url = 'https://api.tinyurl.com'
    headers = 'Bearer 7Mouwis7Xz5zml4XU63pvDuzYIOJrLyWvV8LTLSDBkimeA9eU5zTJ4z1FYBI'


    def shorten(self, url):
        """
        No validation
        Synchronous requests in asynchronous process
        Obfuscation of the actual endpoint (shorten instead of create)
        No abstraction in dataclass in result
        """
        body = {'url': url}
        session = requests.Session()
        response = session.post(f'{self.base_url}/create', json=body, headers=self.headers)
        return response.json()