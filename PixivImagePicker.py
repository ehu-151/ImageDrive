from pixivpy3 import *
from PixivDriveSettingJsonAdapter import PixivDriveSettingJsonAdapter
from PixivAccountJsonAdapter import PixivAccountJsonAdapter

import json


class PixivImagePicker:
    """
    Pixivの画像をバイナリファイルで取得するクラス。

    Hint:
    #save_images_by_tag: tagを指定して画像を返します。
    """

    def __init__(self):
        self.aapi = AppPixivAPI()
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

    def save_images_by_tags(self, tags,times):
        """
        tagを指定して画像を返します。

        :param tags: タグ
        :return: image: 画像
        """
        self.__login()
        json_result = self.aapi.search_illust(word=tags, req_auth=True)
        # 枚数分だけダウンロード
        for illust in json_result.illusts[:times]:
            self.__download(illust.image_urls['large'])

    def __download(self, image_url):
        self.aapi.download(image_url, path=r'C:\Users\kaikoro\.PyCharmCE2017.2\config\scratches\image')
        print("ダウンロードしました")


def main():
    # インスタンス生成
    picker = PixivImagePicker()
    # タグで画像を取得
    picker.save_images_by_tags("背景",3)


if __name__ == '__main__':
    main()
