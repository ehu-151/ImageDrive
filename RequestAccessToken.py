import datetime
import requests

from OneDriveTokenJsonAdapter import OneDriveTokenJsonAdapter


class RequestAccessToken:
    def __init__(self):
        self.__access_token = None
        self.__refresh_token = None
        self.__redirect_url = "https://localhost:3000/returned"
        self.__scope = "Files.ReadWrite.All offline_access"

    def get_access_token(self):
        """
        アクセストークンを取得します。

        :return: access_token
        """

        # Jsonデータから直近の更新時間をチェック、何も記入されていない場合はエラー
        adapter = OneDriveTokenJsonAdapter()
        form = "%Y-%m-%d %H:%M"
        if adapter.time_stamp != "":
            least_log_time = datetime.datetime.strptime(adapter.time_stamp, form)
        else:
            raise ValueError(
                "timestamp is none value. you must replace Value to '2000-01-01 01:00'  in 'onedrive_token.json'")
        # 現在の時刻
        now_time = datetime.datetime.now()

        # アクセストークンを更新すべきかのチェック
        if now_time - least_log_time >= datetime.timedelta(seconds=60 * 50):
            # アクセストークンが50分以上経過した時と更新ログが設定されてない場合は、更新する
            return self.__refresh_access_token()
        else:
            # 更新無しで'onedrive_token.json'から取得
            return adapter.access_token

    def __refresh_access_token(self):
        """
        リフレッシュトークンからアクセストークンを生成して返します。

        :return: access_token
        """
        config = OneDriveTokenJsonAdapter()
        # URLエンドポイント
        endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
        # bodyのパラメータ
        payload = {"grant_type": "refresh_token", "refresh_token": config.refresh_token, "client_id": config.client_id,
                   "client_secret": config.client_secret, "scope": self.__scope, "redirect_uri": self.__redirect_url}
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=endpoint, data=payload, headers=header)
        if res.status_code == 200:
            # 'onedrive_token.json'に'更新時刻とアクセストークンを書き込むで新しいトークを返す
            form = "%Y-%m-%d %H:%M"
            now_time = datetime.datetime.now().strftime(form)
            json_data = res.json()
            access_token = json_data["access_token"]
            config.save_value(access_token=access_token, timestamp=str(now_time))
            return json_data["access_token"]


def main():
    request = RequestAccessToken()
    access_token = request.get_access_token()
    print(access_token)


if __name__ == '__main__':
    main()
