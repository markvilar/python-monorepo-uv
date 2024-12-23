"""Module for backend runner."""

import uvicorn

from fastapi import FastAPI

from core import Item, User
from utils import logger


app = FastAPI()


@app.get("/")
def read_root():
    """Reads application root."""
    return {"Hello": "World"}


@app.get("/users")
def read_users() -> list[User]:
    """Reads application users."""
    return [User(id=0, name="Phil"), User(id=1, name="Collin")]


@app.get("/items")
def read_items() -> list[Item]:
    """Reads application items."""
    return [Item(id=0), Item(id=1), Item(id=2)]


def main() -> None:
    """Main entrypoint."""
    config: uvicorn.Config = uvicorn.Config("backend.runner:app", host="localhost", port=5000, log_level="info")
    server: uvicorn.Server = uvicorn.Server(config)
    server.run()


if __name__ == "__main__":
    main()
