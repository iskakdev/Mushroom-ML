from fastapi import FastAPI
from mushroom_app.api import predict
import uvicorn


mushroom_app = FastAPI(title='Mushroom')
mushroom_app.include_router(predict.mushroom_predict)


if __name__ == '__main__':
    uvicorn.run(mushroom_app, host='127.0.0.1', port=8000)
