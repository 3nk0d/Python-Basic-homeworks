from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def main_page():
    return {"message":"Main page"}


@app.get("/ping/", status_code=200)
def ping_message():
    return {"message": "pong"}