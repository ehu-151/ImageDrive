"""
PixivDriveを扱うスクリプトファイル。実行するとPixivからOneDriveに画像をアップロードする。
"""

from TwitterPicker import TwitterPicker
from OneDriveAPI import OneDriveAPI
from RequestAccessToken import RequestAccessToken
import json


def main():
    # 設定ファイル読み込み
    with open(r"../config.json", "r", encoding='utf-8_sig') as file:
        json_data = json.load(file)

    # 各設定の変数格納
    twitter_config = json_data["twitter_config"]
    onedrive_config = json_data["onedrive_config"]
    want_image = json_data["want_image"]

    # インスタンス生成
    picker = TwitterPicker(twitter_config["consumer_key"], twitter_config["consumer_secret"],
                           twitter_config["access_token"], twitter_config["access_secret"])
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
        print("「" + str(tag) + "」で画像をダウンロード")
        # ハッシュタグで画像を取得
        image_binary = picker.get_binary_image_by_word(str(tag), int(want_image["num_of_image"]))
        for i, image_binary in enumerate(image_binary):
            print("画像のダウンロード開始")

            name = str(i + 1) + ".jpg"
            drive.simple_upload_file("WindowsLockPicture", name, image_binary, "image/jpeg")
            print("完了：" + name)


main()
