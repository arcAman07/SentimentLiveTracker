# SentimentLiveTracker

Note : A file named **config.py** must be created with code :
``` 
from pydantic import BaseSettings


class Settings(BaseSettings):
    TPCK: str = "{Your key}"
    TSCK: str = "{Your key}"
    TPAK: str = "{Your key}"
    TSAK: str = "{Your key}"


settings = Settings()
 ```



Dataset URLs:


1)IMDB Dataset: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews


2)Tweet Analysis Dataset : https://www.kaggle.com/abhi8923shriv/sentiment-analysis-dataset

