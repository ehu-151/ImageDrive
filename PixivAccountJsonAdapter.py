from BasePixivDriveJsonAdapter import BasePixivDriveJsonAdapter


class PixivAccountJsonAdapter(BasePixivDriveJsonAdapter):
    def __init__(self):
        super().__init__()
        self.pixiv_id = None
        self.password = None

    def load_json(self, path, encoding):
        super(PixivAccountJsonAdapter, self).load_json(path, encoding)
        self.__load_value(self.json_data)

    def __load_value(self, json_data):
        # 初期化
        self.pixiv_id = json_data["pixiv_id"]
        self.password = json_data["password"]


def main():
    # インスタンス生成
    config = PixivAccountJsonAdapter()
    # パスとエンコーディングを指定してJsonの読み込み
    config.load_json(r"..\..\.PyCharmCE2017.2\config\scratches\client.json", "utf-8_sig")
    # メールアドレスを取得
    pixiv_id = config.pixiv_id
    print(pixiv_id)
    # パスワードを取得
    password = config.password
    print(password)


if __name__ == '__main__':
    main()
