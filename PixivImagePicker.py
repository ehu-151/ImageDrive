from pixivpy3 import AppPixivAPI
import json


class PixivImagePicker(AppPixivAPI):
    """
    Pixivの画像をバイナリファイルで取得するクラス。AppPixivAPIを継承しています。

    Hint:
    #login()は不要、コンストラクタ生成時に自動ログインします。
    #get_image_urls_by_tag(): タグと指定したタグの画像の枚数を指定して画像のurlリストを返します。
    #download_binary()で画像のurlを指定して画像のバイナリを返します。複数のバイナリが欲しい場合はfor分で回してください。
    """

    def __init__(self, username: str, password: str):
        super(PixivImagePicker, self).__init__()
        self.login(username, password)

    def get_image_urls_by_tag(self, tag: str, times: int) -> str:
        """
          tagを指定して画像のurlを返します。

          :param tag: タグ
          :param times: 指定タグの画像の取得数
          :return urls: 指定タグの画像のurlリスト
          """
        urls = []
        num = 30
        for i in range(0, int(times / 30) + 1):
            if i == 0:
                json_result = self.search_illust(word=tag, req_auth=True)
            else:
                next_qs = self.parse_qs(json_result.next_url)
                if next_qs is None:
                    return urls
                # 空白が'+'に変換されてしまうので、ここで空白に置き換え
                next_qs["word"] = str(next_qs["word"]).replace('+', ' ')
                json_result = self.search_illust(**next_qs)

            # 枚数分だけダウンロード
            if times - (i * 30) < 30: num = times - (i * 30)
            for illust in json_result.illusts[:num]:
                urls.append(illust["image_urls"]["large"])
        return urls

    def download_binary(self, url: str, referer='https://app-api.pixiv.net/'):
        """
        指定した画像urlをバイナリで取得します。

        :param url: 画像url
        :param referer:
        :return image_binary: 指定した画像のバイナリ
        """
        # Write stream to file
        response = self.requests_call('GET', url, headers={'Referer': referer}, stream=True)
        image_binary = response.content
        return image_binary


def main():
    # 設定ファイル読み込み
    with open(r"../config.json", "r", encoding='utf-8_sig') as file:
        json_data = json.load(file)

    pixiv_config = json_data["pixiv_config"]
    picker = PixivImagePicker(pixiv_config["pixiv_id"], pixiv_config["password"])

    urls = picker.get_image_urls_by_tag("女の子", 3)
    image_binay = picker.download_binary(urls[0])

    hoge = picker.search_illust("女の子", req_auth=True)
    print(str(hoge).replace("\'", '\"'))


if __name__ == '__main__':
    main()
