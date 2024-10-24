from dataclasses import dataclass
from datetime import date
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return "server is running"
