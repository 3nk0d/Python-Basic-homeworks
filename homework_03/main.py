from fastapi import FastAPI
from views.views import router as rout_views

app = FastAPI()
app.include_router(rout_views)

@app.get("/")
def main_page():
    return {"message":"Main page"}


@app.get("/ping/", status_code=200)
def ping_message():
    return {"message": "pong"}