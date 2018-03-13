
from pixivpy3 import AppPixivAPI


class MyAppPixivAPI(AppPixivAPI):
    def download_binary(self, url, referer='https://app-api.pixiv.net/'):
        # Write stream to file
        response = self.requests_call('GET', url, headers={'Referer': referer}, stream=True)
        return response.content


def main():
    pass


if __name__ == '__main__':
    main()
