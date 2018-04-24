from pixivpy3 import AppPixivAPI
from PixivAccountJsonAdapter import PixivAccountJsonAdapter
from PixivDriveSettingJsonAdapter import PixivDriveSettingJsonAdapter


class PixivImagePicker(AppPixivAPI):
    """
    Pixivの画像をバイナリファイルで取得するクラス。AppPixivAPIを継承しています。

    Hint:
    #login()でログイン
    #get_image_url_by_tags(): tagを指定して画像のurlを返します。
    #download_binary()で画像のurlを指定して画像のバイナリを返します。
    """

    def __init__(self, username, password):
        super(PixivImagePicker, self).__init__()
        self.login(username, password)

    def get_image_url_by_tags(self, tags, times):
        """
        tagを指定して画像のurlを返します。

        :param tags: タグ
        :param times: 指定タグの画像の取得数
        :return: なし
        """
        json_result = self.search_illust(word=tags, req_auth=True)
        # 枚数分だけダウンロード
        urls = []
        for illust in json_result.illusts[:int(times)]:
            urls.append(illust["image_urls"]["large"])
        return urls

    def download_binary(self, url, referer='https://app-api.pixiv.net/'):
        # Write stream to file
        response = self.requests_call('GET', url, headers={'Referer': referer}, stream=True)
        return response.content


def main():
    account = PixivAccountJsonAdapter()
    account.load_json()
    username = account.pixiv_id
    password = account.password

    pixiv_setting = PixivDriveSettingJsonAdapter()

    # インスタンス生成
    picker = PixivImagePicker(username, password)
    print(pixiv_setting.tags)
    # タグで画像を取得
    urls = picker.get_image_url_by_tags(pixiv_setting.tags[0], 1)
    print(urls)
    for url in urls:
        image = picker.download_binary(url)
        print(image)


if __name__ == '__main__':
    main()
