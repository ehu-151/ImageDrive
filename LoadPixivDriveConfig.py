import json

from PixivDriveConfig import PixivDriveConfig


class LoadPixivDriveConfig(PixivDriveConfig):
    """
    PixivDriveのPixivDriveConfig.jsonをパースし、値を取得する為のクラスです。
    初めに#load_json()でJsonファイルを読み込みます。後は自由に#tagsなどでValueを受け取ります。
    """

    def __init__(self):
        super().__init__()

    def load_json(self, path, encoding):
        """
        Jsonファイルを読み込みます。
        :param path: Jsonファイルのパス
        :param encoding: Windowsの場合はutf-8_sig
        :return: なし
        """
        # ファイルを開く
        f = open(path, 'r', encoding=encoding)
        json_data = json.load(f)
        self.__load_value(json_data)

    def __load_value(self, json_data):
        """
        Json#load()を引数にとり、フィールドにValueを格納します。
        :param json_data: Json#load()の返り値
        :return: なし
        """
        # 初期化
        self.tags = json_data["want_image"]["tag"]
        self.num_of_image = int(json_data["want_image"]["num_of_image"])
        self.interval = int(json_data["interval"])


def main():
    # インスタンス生成
    config = LoadPixivDriveConfig()
    # パスとエンコーディングを指定してJsonの読み込み
    config.load_json("PixivDriveConfig.json", "utf-8_sig")

    # タグ取得
    tags = config.tags
    print(tags)
    # 画像数を取得
    num_of_image = config.num_of_image
    print(num_of_image)
    # 更新間隔を取得
    interval = config.interval
    print(interval)


if __name__ == '__main__':
    main()
