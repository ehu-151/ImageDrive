import json


class PixivDriveConfig:
    def __init__(self):
        self.json_data = None

    def load_json(self, path, encoding):
        f = open(path, 'r', encoding=encoding)
        self.json_data = json.load(f)

    def get_tags(self):
        return self.json_data["want_image"]["tag"]

    def get_num_of_image(self):
        return self.json_data["want_image"]["num_of_image"]

    def get_interval(self):
        return self.json_data["interval"]


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
