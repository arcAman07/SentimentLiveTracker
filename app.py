import uvicorn
from fastapi import FastAPI
from config import settings
from tweet_generator import tweet_generator

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, stranger'}


@app.get('/{name}')
def get_name(name: str):
    TPCK = settings.TPCK
    TSCK = settings.TSCK
    TPAK = settings.TPAK
    TSAK = settings.TSAK
    twitter_bot = tweet_generator.PersonTweeter(name,TPCK,TSCK,TPAK,TSAK)
    random_tweet = twitter_bot.generate_random_tweet()
    random_tweet = random_tweet
    return {'Tweet': random_tweet}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)