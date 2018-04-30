from pixivpy3 import AppPixivAPI


class PixivImagePicker(AppPixivAPI):
    """
    Pixivの画像をバイナリファイルで取得するクラス。AppPixivAPIを継承しています。

    Hint:
    #login()は不要、コンストラクタ生成時に自動ログインします。
    #get_image_urls_by_tag(): タグと指定したタグの画像の枚数を指定して画像のurlリストを返します。
    #download_binary()で画像のurlを指定して画像のバイナリを返します。複数のバイナリが欲しい場合はfor分で回してください。
    """

    def __init__(self, username, password):
        super(PixivImagePicker, self).__init__()
        self.login(username, password)

    def get_image_urls_by_tag(self, tag, times):
        """
        tagを指定して画像のurlを返します。

        :param tag: タグ
        :param times: 指定タグの画像の取得数
        :return urls: 指定タグの画像のurlリスト
        """
        json_result = self.search_illust(word=tag, req_auth=True)
        # 枚数分だけダウンロード
        urls = []
        for illust in json_result.illusts[:int(times)]:
            urls.append(illust["image_urls"]["large"])
        return urls

    def download_binary(self, url, referer='https://app-api.pixiv.net/'):
        """
        指定した画像urlをバイナリで取得します。

        :param url: 画像url
        :param referer:
        :return image_binary: 指定した画像のバイナリ
        """
        # Write stream to file
        response = self.requests_call('GET', url, headers={'Referer': referer}, stream=True)
        image_binary = response.content
        return image_binary


def main():
    picker = PixivImagePicker("", "")
    urls = picker.get_image_urls_by_tag("", 3)
    image_binay = picker.download_binary(urls[0])
    print(image_binay)


if __name__ == '__main__':
    main()
