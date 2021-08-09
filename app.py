from tensorflow import keras
import uvicorn
from config import settings
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
# from config import settings
from tweet_generator import tweet_generator
import tensorflow as tf
import numpy as np
tweet = ''
app = FastAPI()
model = tf.keras.models.load_model('SentimentAnalysis')
class Reviews(BaseModel):
    text: str


@ app.get('/')
def index():
    return {'message': 'Welcome to the Text Classifier Engine'}


@ app.get('/generate-tweet/{name}')
def get_name(name: str):
    sentiment = ''
    TPCK = settings.TPCK
    TSCK = settings.TSCK
    TPAK = settings.TPAK
    TSAK = settings.TSAK
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

@app.get('/predict/{sentence}')
def predict_review(sentence:str):
    sentiment = ''
    prediction = model.predict([sentence])
    result = prediction.tolist()[0][0]
    if result>=0.5:
        sentiment = 'Positive sentiment is associated with this tweet'
    else:
        sentiment = 'Negative sentiment is associated with this tweet'
    return {
        'prediction': result,
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
