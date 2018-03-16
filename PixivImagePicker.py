from pixivpy3 import AppPixivAPI
from PixivAccountJsonAdapter import PixivAccountJsonAdapter
from PixivDriveSettingJsonAdapter import PixivDriveSettingJsonAdapter


class PixivImagePicker(AppPixivAPI):
    """
    Pixivの画像をバイナリファイルで取得するクラス。AppPixivAPIを継承しています。

    Hint:
    #save_images_by_tag: tagを指定して画像を返します。
    """

    def get_image_url_by_tags(self, tags, times):
        """
        tagを指定して画像を返します。

        :param tags: タグ
        :param times: 指定タグの画像の取得数
        :return: なし
        """
        self.__login()
        json_result = self.search_illust(word=tags, req_auth=True)
        # 枚数分だけダウンロード
        return json_result.illusts[:times]

    def download_binary(self, url, referer='https://app-api.pixiv.net/'):
        # Write stream to file
        response = self.requests_call('GET', url, headers={'Referer': referer}, stream=True)
        return response.content


def main():
    account = PixivAccountJsonAdapter()
    account.load_json(r"..\..\.PyCharmCE2017.2\config\scratches\client.json", "utf-8_sig")
    username = account.pixiv_id
    password = account.password

    pixiv_setting = PixivDriveSettingJsonAdapter()

    # インスタンス生成
    picker = PixivImagePicker()
    picker.login(username, password)
    print(pixiv_setting.tags)
    # タグで画像を取得
    # picker.get_image_url_by_tags(pixiv_sttting.tags[0], 1)


if __name__ == '__main__':
    main()
