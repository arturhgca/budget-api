from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Union

from beancount.core.data import Transaction, Commodity, Open

from budget.ledger import Ledger

logical_ledger = Ledger(path="beancountfiles/logical.beancount")
physical_ledger = Ledger(path="beancountfiles/physical.beancount")


class Item(ABC):
    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs) -> Item:
        return NotImplemented

    @classmethod
    @abstractmethod
    def get_all(cls) -> List[Item]:
        return NotImplemented

    @classmethod
    @abstractmethod
    def get(cls, uid: str) -> Item:
        return NotImplemented

    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError

    def as_dict(self) -> dict:
        return vars(self)

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_beancount(cls, **kwargs) -> Item:
        return NotImplemented

    @abstractmethod
    def to_beancount(self) -> Union[Commodity, Open, Transaction]:
        return NotImplemented
