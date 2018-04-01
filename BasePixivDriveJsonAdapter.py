import json


class BasePixivDriveJsonAdapter:
    """
    Jsonパーサの基礎クラスです。load_jsonを保持します。
    """

    def __init__(self):
        self.json_data = None
        self.path = None
        self.encoding = "utf-8_sig"

    def load_json(self):
        """
        Jsonファイルを読み込みます。
        :param path: Jsonファイルのパス
        :param encoding: Windowsの場合はutf-8_sig
        :return: なし
        """
        # ファイルを開く
        f = open(self.path, 'r', encoding=self.encoding)
        self.json_data = json.load(f)

    def __load_value(self, json_data):
        """valueを読み込みフィールドに格納します。
        :param json_data: jsonクラスでパースした文字列
        :return: なし
        """
        pass
