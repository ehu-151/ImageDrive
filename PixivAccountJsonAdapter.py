from BasePixivDriveJsonAdapter import BasePixivDriveJsonAdapter


class PixivAccountJsonAdapter(BasePixivDriveJsonAdapter):
    def __init__(self):
        super().__init__()
        self.email = None
        self.password = None

    def load_json(self, path, encoding):
        super(PixivAccountJsonAdapter, self).load_json(path, encoding)
        self.__load_value(self.json_data)

    def __load_value(self, json_data):
        # 初期化
        self.tags = json_data["email"]
        self.num_of_image = json_data["password"]
