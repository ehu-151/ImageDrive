from BasePixivDriveJsonAdapter import BasePixivDriveJsonAdapter


class PixivAccountJsonAdapter(BasePixivDriveJsonAdapter):
    """
    Pixivアカウント情報を返します。Pixivアカウント情報のJsonAdapterです。
    """

    def __init__(self):
        super().__init__()
        self.pixiv_id = None
        self.password = None
        self.path = r"..\client.json"
        self.__load_json()

    def __load_json(self):
        super(PixivAccountJsonAdapter, self).load_json()
        self.__load_value(self.json_data)

    def __load_value(self, json_data):
        # 初期化
        self.pixiv_id = json_data["pixiv_id"]
        self.password = json_data["password"]


def main():
    # インスタンス生成
    config = PixivAccountJsonAdapter()
    # メールアドレスを取得
    pixiv_id = config.pixiv_id
    print(pixiv_id)
    # パスワードを取得
    password = config.password
    print(password)


if __name__ == '__main__':
    main()
