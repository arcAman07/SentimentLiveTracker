from tensorflow import keras
import uvicorn
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
# from config import settings
from tweet_generator import tweet_generator
import tensorflow as tf
import numpy as np
tweet = ''
app = FastAPI()
model = tf.keras.models.load_model('C:/Users/amans/OneDrive/Documents/All Machine Learning/ML Models/SentimentAPI_twitter/SentimentAnalysis')
class Reviews(BaseModel):
    text: str


@ app.get('/')
def index():
    return {'message': 'Welcome to the Text Classifier Engine'}


@ app.get('/generate-tweet/{name}')
def get_name(name: str):
    sentiment = ''
    TPCK = "xVkTAd1wDA3ySd2GY2TWARaEi"
    TSCK = "yrKhWbwj9P3s2aUgl8ho4b4TKdcCXYk7z1PDTR6jqvuusXzN4k"
    TPAK = "1299392071468425216-LUkjtSHB9cVXnlkAebcgoLIreWWNme"
    TSAK = "u5h73AaFqJP1X92BohYsNEAeg2ZRGw0ofFbgvKxiP47it"
    twitter_bot = tweet_generator.PersonTweeter(name, TPCK, TSCK, TPAK, TSAK)
    random_tweet = twitter_bot.generate_random_tweet()
    tweet = random_tweet
    result = model.predict([tweet])
    if result>=0.5:
        sentiment = 'Positive sentiment is associated with this tweet'
    else:
        sentiment = 'Negative sentiment is associated with this tweet'
    return {'Tweet': random_tweet,
            'Sentiment Analysis':sentiment
            }

@app.post('/predict')
def predict_review(data:Reviews):
    sentiment = ''
    received = data.dict()
    text = received['text']
    prediction = model.predict([text])
    result = prediction.tolist()[0][0]
    if result>=0.5:
        sentiment = 'Positive sentiment is associated with this tweet'
    else:
        sentiment = 'Negative sentiment is associated with this tweet'
    return {
        'prediction': result,
        'Sentiment Analysis':sentiment
    }

    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
