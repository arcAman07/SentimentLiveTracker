from tensorflow import keras
import uvicorn
from fastapi import FastAPI
from config import settings
from tweet_generator import tweet_generator
import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
app = FastAPI()

model = keras.models.load_model("TextSentiment_Analysis")

tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")


@ app.get('/')
def index():
    return {'message': 'Hello, stranger'}


@ app.get('/generate-tweet/{name}')
def get_name(name: str):
    TPCK = settings.TPCK
    TSCK = settings.TSCK
    TPAK = settings.TPAK
    TSAK = settings.TSAK
    twitter_bot = tweet_generator.PersonTweeter(name, TPCK, TSCK, TPAK, TSAK)
    random_tweet = twitter_bot.generate_random_tweet()
    random_tweet = random_tweet
    return {'Tweet': random_tweet}


@ app.get('/predict-sentiment/{str}')
def get_name(str: str):
    sentence = [str]
    print(sentence)
    seq = tokenizer.texts_to_sequences(sentence)
    print(seq)
    padded = pad_sequences(seq, maxlen=120,
                           padding="post", truncating="post")
    prediction = model.predict(padded)
    return {'Predicted sentiment': prediction}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
