from BasePixivDriveJsonAdapter import BasePixivDriveJsonAdapter
import json


class OneDriveTokenJsonAdapter(BasePixivDriveJsonAdapter):
    def __init__(self):
        super().__init__()
        self.client_id = None
        self.client_secret = None
        self.refresh_token = None
        self.access_token = None
        self.time_stamp = None
        self.path = r"..\onedrive_token.json"
        self.__load_json()

    def __load_json(self):
        super(OneDriveTokenJsonAdapter, self).load_json()
        self.__load_value(self.json_data)

    def __load_value(self, json_data):
        # 初期化
        self.client_id = json_data["client_id"]
        self.client_secret = json_data["client_secret"]
        self.refresh_token = json_data["refresh_token"]
        self.access_token = json_data["access_token"]
        self.time_stamp = json_data["time_stamp"]

    def save_value(self, access_token=None, timestamp=None):
        """
        KeyとValueを指定してJsonを保存します。

        :param access_token:
        :param timestamp:
        :return: なし
        """
        if access_token is not None:
            self.access_token = access_token
        if timestamp is not None:
            self.time_stamp = timestamp

        ys = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "access_token": self.access_token,
            "time_stamp": self.time_stamp
        }
        fw = open(self.path, 'w')
        # ココ重要！！
        # json.dump関数でファイルに書き込む
        json.dump(ys, fw, indent=2)


def main():
    config = OneDriveTokenJsonAdapter()
    print(config.access_token)
    print(config.refresh_token)
    print(config.time_stamp)


if __name__ == '__main__':
    main()
