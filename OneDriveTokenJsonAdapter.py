from BasePixivDriveJsonAdapter import BasePixivDriveJsonAdapter


class OneDriveTokenJsonAdapter(BasePixivDriveJsonAdapter):
    def __init__(self):
        super().__init__()
        self.access_token = None
        self.refresh_token = None
        self.time_stamp = None
        self.__path = r"..\onedrive_token.json"
        self.__load_json()

    def __load_json(self):
        super(OneDriveTokenJsonAdapter, self).load_json(self.__path, "utf-8_sig")
        self.__load_value(self.json_data)

    def __load_value(self, json_data):
        # 初期化
        self.access_token = json_data["access_token"]
        self.refresh_token = json_data["refresh_token"]
        self.time_stamp = json_data["time_stamp"]


def main():
    config = OneDriveTokenJsonAdapter()
    print(config.access_token)
    print(config.refresh_token)
    print(config.time_stamp)


if __name__ == '__main__':
    main()
