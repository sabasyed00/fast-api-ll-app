from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Load the model
sentiment_pipeline = pipeline("sentiment-analysis")

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    result = sentiment_pipeline(input.text)[0]
    return {"label": result["label"], "score": result["score"]}
