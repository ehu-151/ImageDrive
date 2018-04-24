"""
PixivDriveを扱うスクリプトファイル。実行するとPixivからOneDriveに画像をアップロードする。
"""
from box import Box
from PixivImagePicker import PixivImagePicker
from OneDriveAPI import OneDriveAPI


def main():
    # 設定ファイル読み込み
    with open(r"C:\Users\kaikoro\PycharmProjects\config.json", "r", encoding='utf-8_sig') as file:
        whole_str = file.read()
    # 変数'user_box'内でBoxオブジェクトの作成
    user_box = Box.from_json(whole_str)
    print(user_box)
    # pixivの設定
    pixiv_config = user_box.pixiv_config
    onedrive_config = user_box.onedrive_config
    want_image = user_box.want_image

    print(user_box)  # Michel

    # 設定ファイルからアカウント情報を取得

    # インスタンス生成
    picker = PixivImagePicker(pixiv_config.pixiv_id, pixiv_config.password)
    drive = OneDriveAPI()

    print("OneDriveにアップロードします。")
    # タグでループ
    for tag in want_image.tag:
        print("「" + str(tag) + "」で画像を取得")
        image_urls = picker.get_image_url_by_tags(tag, want_image.num_of_image)
        # タグで画像を取得
        print(str(len(image_urls)) + "枚ダウンロード")
        for i, image_url in enumerate(image_urls):
            print("画像のダウンロード開始")
            image = picker.download_binary(image_url)
            name = str(tag) + "_" + str(i + 1) + ".jpg"
            drive.simple_upload_file("WindowsLockPicture", name, image, "image/jpeg")
            print("完了：" + name)


main()
