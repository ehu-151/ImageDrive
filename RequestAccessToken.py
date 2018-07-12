import datetime
import requests
import json


class RequestAccessToken:
    def __init__(self, onedrive_config):
        self.__client_id = onedrive_config["client_id"]
        self.__client_secret = onedrive_config["client_secret"]
        self.__refresh_token = onedrive_config["refresh_token"]
        self.__access_token = onedrive_config["access_token"]
        self.__time_stamp = onedrive_config["time_stamp"]
        self.__onedrive_config = onedrive_config
        self.__redirect_url = "https://localhost:3000/returned"
        self.__scope = "Files.ReadWrite.All offline_access"

    def get_onedrive_json(self):
        """
        config.json用のonedrive_configを更新します。
        具体的な内容は、refresh_tokenで取得したaccess_tokenとその時の時刻をJsonにしたonedrive_configを返します。

        :return: onedrive_config
        """

        # Jsonデータから直近の更新時間をチェック、何も記入されていない場合はエラー
        form = "%Y-%m-%d %H:%M"
        if self.__time_stamp != "":
            least_log_time = datetime.datetime.strptime(self.__time_stamp, form)
        else:
            # 更新日が記入されていなかったら例外を出す。
            raise ValueError(
                "timestamp is none value. you must replace Value to '2000-01-01 01:00'  in 'config.json'")
        # 現在の時刻を取得
        now_time = datetime.datetime.now()

        # アクセストークンを更新すべきかのチェック
        if now_time - least_log_time >= datetime.timedelta(seconds=60 * 50):
            # アクセストークンが50分以上経過した時と更新ログが設定されてない場合は、更新する
            return self.__refresh_access_token()
        else:
            # 更新無しで'onedrive_token.json'から取得
            return self.__onedrive_config

    def __refresh_access_token(self):
        """
        リフレッシュトークンからアクセストークンを生成して返します。

        :return: access_token
        """
        # URLエンドポイント
        endpoint = "https://login.microsoftonline.com/common/oauth2/v2.0/token"
        # bodyのパラメータ
        payload = {"grant_type": "refresh_token", "refresh_token": self.__refresh_token, "client_id": self.__client_id,
                   "client_secret": self.__client_secret, "scope": self.__scope, "redirect_uri": self.__redirect_url}
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        res = requests.post(url=endpoint, data=payload, headers=header)
        if res.status_code == 200:
            # 'onedrive_token.json'に'更新時刻とアクセストークンを書き込むで新しいトークを返す
            form = "%Y-%m-%d %H:%M"
            now_time = datetime.datetime.now().strftime(form)
            res_data = res.json()

            self.__onedrive_config["access_token"] = res_data["access_token"]
            self.__onedrive_config["time_stamp"] = str(now_time)
            return self.__onedrive_config


def main():
    # 設定ファイル読み込み
    with open(r"C:\Users\kaikoro\PycharmProjects\config.json", "r", encoding='utf-8_sig') as file:
        json_data = json.load(file)
    onedrive_config = json_data["onedrive_config"]
    request_token = RequestAccessToken(onedrive_config)
    onedrive_config = request_token.get_onedrive_json()
    print(onedrive_config)


if __name__ == '__main__':
    main()
