"""
You can get tweet and image using this class.

このクラスはツイートと画像(バイナリ)を検索し、返すクラス
"""
import tweepy
import requests
import json


class TwitterPicker:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_secret: str):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_secret = access_secret
        self.api = self.setup()

    def get_binary_image_by_word(self, word: str, num: int = 5):
        """
        ツイートのidを取得します
        :param word:
        :param only_image:
        :return:
        """

        public_tweets = self.api.search(word, lang="ja")
        now_num = 0
        image_binary = []

        for tweet in public_tweets:
            tweet_json = json.loads(json.dumps(tweet._json))
            try:
                for media in tweet_json["entities"]["media"]:
                    res = requests.get(media["media_url"], stream=True)
                    image_binary.append(res.content)
                    now_num += 1
                    if (now_num == num): return image_binary

            except KeyError:
                # mediaがないとき
                pass

    def get_image_binary(self, image_url):
        """
        指定したidから画像をバイナリで取得します。
        :param image_url:
        :return:
        """
        pass

    def setup(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)

        api = tweepy.API(auth)
        return api


def main():
    # 設定ファイル読み込み
    with open(r"../config.json", "r", encoding='utf-8_sig') as file:
        json_data = json.load(file)

    consumer_key = json_data["twitter_config"]["consumer_key"]
    consumer_secret = json_data["twitter_config"]["consumer_secret"]
    access_token = json_data["twitter_config"]["access_token"]
    access_secret = json_data["twitter_config"]["access_secret"]

    tweetAPI = TwitterPicker(consumer_key, consumer_secret, access_token, access_secret)
    image_binary = tweetAPI.get_binary_image_by_word("#背景", 10)
    print(image_binary)


if __name__ == '__main__':
    main()
