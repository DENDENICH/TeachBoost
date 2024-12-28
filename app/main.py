from fastapi import FastAPI
from settings import settings
import uvicorn

app = FastAPI()

if __name__ == '__main__':
    uvicorn.run(
        app,
        host=settings.address.HOST,
        port=settings.address.PORT
    )