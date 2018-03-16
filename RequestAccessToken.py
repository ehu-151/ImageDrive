from OneDriveTokenJsonAdapter import OneDriveTokenJsonAdapter
from datetime import datetime


class RequestAccessToken:
    def __init__(self):
        self.__access_token = None
        self.__refresh_token = None

    def get_access_token(self):
        """
        アクセストークンを取得します。

        :return: access_token
        """
        adapter = OneDriveTokenJsonAdapter()
        now_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        # アクセストークンを更新すべきかのチェック
        if adapter.time_stamp == "":
            pass
        elif adapter.time_stamp > now_time - 3600:
            return adapter.access_token
        else:
            pass


def main():
    pass


if __name__ == '__main__':
    main()
