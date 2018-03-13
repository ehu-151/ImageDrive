from pixivpy3 import *
from PixivDriveSettingJsonAdapter import PixivDriveSettingJsonAdapter
from PixivAccountJsonAdapter import PixivAccountJsonAdapter
import urllib.request
import io
import requests
import json
from MyAppPixivAPI import MyAppPixivAPI


class PixivImagePicker:
    """
    Pixivの画像をバイナリファイルで取得するクラス。

    Hint:
    #save_images_by_tag: tagを指定して画像を返します。
    """

    def __init__(self):
        self.aapi = MyAppPixivAPI()
        # アカウント情報(id, password)を格納
        self.__init_setting()
        pass

    def __init_setting(self):
        """
        PixivAccountJsonAdapter.pyからアカウントのidとパスワードの読み込み。

        :return: なし
        """
        account = PixivAccountJsonAdapter()
        account.load_json(r"..\..\.PyCharmCE2017.2\config\scratches\client.json", "utf-8_sig")
        self.pixiv_id = account.pixiv_id
        self.password = account.password

    def __login(self):
        """
        Pixivアカウントにログインします。

        :param pixiv_id: emailアドレス
        :param password: パスワード
        :return: なし
        """
        try:
            self.aapi.login(self.pixiv_id, self.password)
            print("ログイン成功")
        except PixivError:
            print("ログイン失敗")

    def get_image_url_by_tags(self, tags, times):
        """
        tagを指定して画像を返します。

        :param tags: タグ
        :param times: 指定タグの画像の取得数
        :return: なし
        """
        self.__login()
        json_result = self.aapi.search_illust(word=tags, req_auth=True)
        # 枚数分だけダウンロード
        return json_result.illusts[:times]

    def download_binary(self,image_url):
        return self.aapi.download_binary(image_url)

    def __download(self, image_url):
        return self.aapi.download_binary(image_url)


def main():
    # インスタンス生成
    picker = PixivImagePicker()
    # タグで画像を取得
    picker.get_image_url_by_tags("背景", 1)


if __name__ == '__main__':
    main()
