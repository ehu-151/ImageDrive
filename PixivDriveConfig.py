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
    config = PixivDriveConfig()
    config.load_json("PixivDriveConfig.json", "utf-8_sig")
    tags = config.get_tags()
    print(tags)
    num_of_image = config.get_num_of_image()
    print(num_of_image)
    interval = config.get_interval()
    print(interval)


if __name__ == '__main__':
    main()
