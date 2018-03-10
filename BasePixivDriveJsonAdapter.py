import json


class BasePixivDriveJsonAdapter:
    def __init__(self):
        self.json_data = None

    def load_json(self, path, encoding):
        """
        Jsonファイルを読み込みます。
        :param path: Jsonファイルのパス
        :param encoding: Windowsの場合はutf-8_sig
        :return: なし
        """
        # ファイルを開く
        f = open(path, 'r', encoding=encoding)
        self.json_data = json.load(f)

    def __load_value(self, json_data):
        pass
