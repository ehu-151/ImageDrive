import requests


class OneDriveAPI:
    def __init__(self, token):
        self.endpoint = "https://graph.microsoft.com/v1.0"
        self.headers = {"Authorization": token}

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
    pass


if __name__ == '__main__':
    main()
