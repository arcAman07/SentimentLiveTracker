
from tweet_generator import tweet_generator
TPCK = "xVkTAd1wDA3ySd2GY2TWARaEi"
TSCK = "yrKhWbwj9P3s2aUgl8ho4b4TKdcCXYk7z1PDTR6jqvuusXzN4k"
TPAK = "1299392071468425216-LUkjtSHB9cVXnlkAebcgoLIreWWNme"
TSAK = "u5h73AaFqJP1X92BohYsNEAeg2ZRGw0ofFbgvKxiP47it"
twitter_bot = tweet_generator.PersonTweeter('@TanmaysuchAnoob',TPCK,TSCK,TPAK,TSAK)
random_tweet = twitter_bot.generate_random_tweet()
print(random_tweet)
