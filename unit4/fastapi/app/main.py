from fastapi import FastAPI
from starlette.responses import JSONResponse
from joblib import load
import pandas as pd

app = FastAPI()

gmm_pipe = load('../models/gmm_pipeline.joblib')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/health', status_code=200)
async def healthcheck():
    return 'GMM Clustering is all ready to go!'


@app.get("/mall/customers/segmentation/params")
def predict(genre: str,	age: int, income: int, spending: int):
    features = {
        'Gender': [genre],
        'Age': [age],
        'Annual Income (k$)': [income],
        'Spending Score (1-100)': [spending]
    }

    obs = pd.DataFrame(features)
    pred = gmm_pipe.predict(obs)
    return JSONResponse(pred.tolist())
