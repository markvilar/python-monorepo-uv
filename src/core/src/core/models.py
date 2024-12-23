"""Module with data models."""

from pydantic import BaseModel


class User(BaseModel):
    """Class representing a user."""

    id: int
    name: str


class Item(BaseModel):
    """Class representing an item."""

    id: int
