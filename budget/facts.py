from __future__ import annotations

from abc import ABC, abstractmethod
from decimal import Decimal
from typing import List
from uuid import uuid4

from beancount.core.amount import Amount
from beancount.core.data import Posting, Transaction
from pendulum import Date

from budget.beancountwrapper import Ledger

logical_ledger = Ledger(path="beancountfiles/logical.beancount")


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
        raise NotImplementedError

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def as_dict(self) -> dict:
        return NotImplemented

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def from_beancount(cls, item: Transaction) -> Fact:
        return NotImplemented

    @abstractmethod
    def to_beancount(self) -> Transaction:
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
        return [
            Allocation.from_beancount(item)
            for item in logical_ledger.transactions
            if item.meta["type"] == 'allocation'
        ]

    @classmethod
    def get(cls, uid: str) -> Allocation:
        return Allocation.from_beancount(logical_ledger.get(uid))

    def update(self,
               source: str,
               destination: str,
               amount: Decimal,
               currency: str,
               date: Date,
               uid: str,
               notes: str = None,
               ) -> None:
        self.source = source
        self.destination = destination
        self.amount = amount
        self.currency = currency
        self.date = date
        self.uid = uid
        self.notes = notes
        self.commit()

    def delete(self) -> None:
        pass

    def as_dict(self) -> dict:
        return vars(self)

    def commit(self):
        self_beancount = self.to_beancount()
        logical_ledger.entries[self.uid] = self_beancount
        logical_ledger.transactions[self.uid] = self_beancount
        logical_ledger.commit()

    @classmethod
    def from_beancount(cls, item: Transaction) -> Allocation:
        source_posting = next((i for i in item.postings if i.units.number < 0))
        destination_posting = next((i for i in item.postings if i.units.number > 0))
        return Allocation(
            source=source_posting.account,
            destination=destination_posting.account,
            amount=destination_posting.units.number,
            currency=destination_posting.units.currency,
            date=item.date,
            uid=item.meta["uid"],
            notes=item.narration,
        )

    def to_beancount(self) -> Transaction:
        return Transaction(
            meta={
                "uid": self.uid,
                "type": "allocation",
            },
            date=self.date,
            flag="*",
            narration=self.notes,
            postings=[
                Posting(
                    account=self.source,
                    units=Amount(
                        number=-self.amount,
                        currency=self.currency,
                    )
                ),
                Posting(
                    account=self.destination,
                    units=Amount(
                        number=self.amount,
                        currency=self.currency,
                    )
                ),
            ]
        )
