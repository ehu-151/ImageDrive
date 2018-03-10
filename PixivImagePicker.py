from PixivDriveSettingJsonAdapter import PixivDriveSettingJsonAdapter
from pixivpy3 import *
import json


class PixivImagePicker:
    """
    Pixivの画像をバイナリファイルで取得するクラス。

    パラメータ
    tag
    num_of_image
    """

    def __init__(self, pixiv_account, pixiv_drive_config):
        self.tag = pixiv_drive_config.tag
        self.num_of_image = pixiv_drive_config.num_of_image
        self.__pixi

    def login(self, id, password):
        aapi = AppPixivAPI()
        aapi.login(id, password)

    def pick(self):
        pass


def main():
    picker = PixivImagePicker()
    f = open(r'../../.PyCharmCE2017.2/config/scratches/client.json', 'r', encoding="utf-8_sig")
    json_data = json.load(f)

    picker.login(json_data[""])


if __name__ == '__main__':
    main()
