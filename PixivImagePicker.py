from pixivpy3 import *

from PixivAccountJsonAdapter import PixivAccountJsonAdapter


class PixivImagePicker:
    """
    Pixivの画像をバイナリファイルで取得するクラス。Pixivアカウントに#loginでログインしてください。
    """

    def __init__(self):
        self.aapi = AppPixivAPI()
        pass

    def login(self, pixiv_id, password):
        """
        Pixivアカウントにログインします。
        :param pixiv_id: emailアドレス
        :param password: パスワード
        :return: なし
        """
        try:
            self.aapi.login(pixiv_id, password)
            print("ログイン成功")
        except PixivError:
            print("ログイン失敗")

    def pick(self):
        pass


def main():
    picker = PixivImagePicker()
    account = PixivAccountJsonAdapter()
    account.load_json(r"..\..\.PyCharmCE2017.2\config\scratches\client.json", "utf-8_sig")
    picker.login(account.pixiv_id, account.password)


if __name__ == '__main__':
    main()
