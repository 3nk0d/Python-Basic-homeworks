from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def main_page():
    return {"message":"Main page"}


@app.get("/ping/")
def ping_message():
    return {"message": "pong"}