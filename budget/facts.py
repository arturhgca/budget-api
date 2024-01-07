from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List
from uuid import uuid4

from pendulum import Date

from budget.beancountwrapper import Ledger

logical_ledger = Ledger(path="../../beancount-ledger/budget/logical.beancount")


class Fact(ABC):
    @classmethod
    @abstractmethod
    def create(cls, *args, **kwargs) -> Fact:
        return NotImplemented

    @classmethod
    @abstractmethod
    def get_all(cls) -> List[Fact]:
        return NotImplemented

    @classmethod
    @abstractmethod
    def get(cls, uid: str) -> Fact:
        return NotImplemented

    @abstractmethod
    def update(self, *args, **kwargs) -> None:
        return NotImplemented

    @abstractmethod
    def delete(self) -> None:
        return NotImplemented

    @abstractmethod
    @property
    def as_dict(self) -> dict:
        return NotImplemented

    @abstractmethod
    def commit(self) -> None:
        return NotImplemented


class Allocation(Fact):
    def __init__(
        self,
        source: str,
        destination: str,
        amount: Decimal,
        currency: str,
        date: Date,
        uid: str,
        notes: str = None,
    ):
        self.source = source
        self.destination = destination
        self.amount = amount
        self.currency = currency
        self.date = date
        self.uid = uid
        self.notes = notes

    @classmethod
    def create(
        cls,
        source: str,
        destination: str,
        amount: Decimal,
        currency: str,
        date: Date,
        notes: str = None,
    ) -> Allocation:
        item = cls(
            source=source,
            destination=destination,
            amount=amount,
            currency=currency,
            date=date,
            uid=str(uuid4()),
            notes=notes,
        )
        item.commit()
        return item

    @classmethod
    def get_all(cls) -> List[Allocation]:
        pass

    @classmethod
    def get(cls, uid: str) -> Allocation:
        pass

    def update(self, *args, **kwargs) -> None:
        pass

    def delete(self) -> None:
        pass

    @property
    def as_dict(self) -> dict:
        return vars(self)

    def commit(self) -> str:
        return (
            f"{self.date.to_date_string()} *"
            f"  uid: {self.uid}"
            f"  {self.destination} {self.amount} {self.currency}"
            f"  {self.source} -{self.amount} {self.currency}"
        )
