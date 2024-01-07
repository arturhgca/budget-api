from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Fact(ABC):
    @abstractmethod
    @classmethod
    def create() -> Fact:
        return NotImplemented

    @abstractmethod
    @classmethod
    def get_all() -> List[Fact]:
        return NotImplemented

    @abstractmethod
    @classmethod
    def get(uid: str) -> Fact:
        return NotImplemented

    @abstractmethod
    def update() -> None:
        return NotImplemented

    @abstractmethod
    def delete() -> None:
        return NotImplemented

    @abstractmethod
    @property
    def as_dict() -> dict:
        return NotImplemented
