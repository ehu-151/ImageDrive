import json


def main():
    f = open(r"PixivDriveConfig.json", 'r', encoding="utf-8_sig")
    json_data = json.load(f)
    print(json_data["want_image"]["tag"])


if __name__ == '__main__':
    main()
