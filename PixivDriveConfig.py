import json


class PixivDriveConfig:
    def __init__(self):
        self.tags = None
        self.num_of_image = None
        self.interval = None

    def load_json(self, path, encoding):
        # ファイルを開く
        f = open(path, 'r', encoding=encoding)
        json_data = json.load(f)
        self.__load_value(json_data)

    def __load_value(self, json_data):
        # 初期化
        self.tags = json_data["want_image"]["tag"]
        self.num_of_image = json_data["want_image"]["num_of_image"]
        self.interval = json_data["interval"]

    def get_tags(self):
        return self.tags

    def get_num_of_image(self):
        return self.num_of_image

    def get_interval(self):
        return self.interval


def main():
    # インスタンス生成
    config = PixivDriveConfig()
    # パスとエンコーディングを指定してJsonの読み込み
    config.load_json("PixivDriveConfig.json", "utf-8_sig")

    # タグ取得
    tags = config.get_tags()
    print(tags)
    # 画像数を取得
    num_of_image = config.get_num_of_image()
    print(num_of_image)
    # 更新間隔を取得
    interval = config.get_interval()
    print(interval)


if __name__ == '__main__':
    main()
