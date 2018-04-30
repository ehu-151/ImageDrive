"""
PixivDriveを扱うスクリプトファイル。実行するとPixivからOneDriveに画像をアップロードする。
"""

from PixivImagePicker import PixivImagePicker
from OneDriveAPI import OneDriveAPI
from RequestAccessToken import RequestAccessToken
import json


def main():
    # 設定ファイル読み込み
    with open(r"../config.json", "r", encoding='utf-8_sig') as file:
        json_data = json.load(file)

    # 各設定の変数格納
    pixiv_config = json_data["pixiv_config"]
    onedrive_config = json_data["onedrive_config"]
    want_image = json_data["want_image"]

    # インスタンス生成
    picker = PixivImagePicker(pixiv_config["pixiv_id"], pixiv_config["password"])
    request_token = RequestAccessToken(onedrive_config)
    json_data["onedrive_config"] = request_token.get_onedrive_json()

    # jsonファイルのonedrive_configを更新
    with open(r"../config.json", "w", encoding='utf-8_sig') as file:
        json.dump(json_data, file, indent=4)

    # OneDriveAPIインスタンス生成
    drive = OneDriveAPI(onedrive_config["access_token"])

    print("OneDriveにアップロードします。")
    # タグでループ
    for tag in want_image["tag"]:
        print("「" + str(tag) + "」で画像を取得")
        image_urls = picker.get_image_urls_by_tag(tag, want_image["num_of_image"])
        # タグで画像を取得
        print(str(len(image_urls)) + "枚ダウンロード")
        for i, image_url in enumerate(image_urls):
            print("画像のダウンロード開始")
            image = picker.download_binary(image_url)
            name = str(tag) + "_" + str(i + 1) + ".jpg"
            drive.simple_upload_file("WindowsLockPicture", name, image, "image/jpeg")
            print("完了：" + name)


main()
