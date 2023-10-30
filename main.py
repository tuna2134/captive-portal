from .utils import accept_ip
from fastapi import FastAPI, Request
from pydanic import BaseModel


app = FastAPI()


@app.get("/")
def authorize(req: Request) -> dict:
    accept_ip(req.client.host)
    return {"status": 200, "message": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=3000)