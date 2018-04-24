import requests
from RequestAccessToken import RequestAccessToken
from PixivImagePicker import PixivImagePicker
from PixivAccountJsonAdapter import PixivAccountJsonAdapter


class OneDriveAPI:
    def __init__(self):
        token = RequestAccessToken()
        self.endpoint = "https://graph.microsoft.com/v1.0"
        self.headers = {"Authorization": token.get_access_token()}

    def simple_upload_file(self, to_folder, file_name, row_file, file_type="text/plain"):
        """
        4MB以下のファイルをアップロードします。
        :return:
        """
        url = self.endpoint + "/me/drive/root:/" + to_folder + "/" + file_name + ":/content"
        self.headers.update({"Content-Type": file_type})
        response = requests.put(url=url, headers=self.headers, data=row_file)
        if 200 <= response.status_code < 300:
            print("アップロード成功")
        else:
            print("アップロード失敗：ステータスコード")
            print(response.status_code)
            print(response.json())


def main():
    account = PixivAccountJsonAdapter()
    account.load_json()
    username = account.pixiv_id
    password = account.password

    # インスタンス生成
    picker = PixivImagePicker()
    picker.login(username, password)
    drive = OneDriveAPI()
    times = 1
    image_urls = picker.get_image_url_by_tags("女の子", times)
    for image_url in image_urls:
        image = picker.download_binary(image_url)
        drive.simple_upload_file("WindowsLockPicture", "hoge.jpg", image, "image/jpeg")


if __name__ == '__main__':
    main()
