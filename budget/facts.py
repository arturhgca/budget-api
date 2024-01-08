from __future__ import annotations

import datetime
from decimal import Decimal
from typing import List, Optional, Tuple
from uuid import uuid4

from beancount.core.amount import Amount
from beancount.core.data import Transaction, Posting

from budget.data import Item, logical_ledger, physical_ledger


class Allocation(Item):
    def __init__(
            self,
            source: str,
            destination: str,
            amount: Decimal,
            currency: str,
            date: datetime.date,
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
            date: datetime.date,
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
            for item in logical_ledger.values()
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
               date: datetime.date,
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

    def commit(self):
        self_beancount = self.to_beancount()
        logical_ledger[self.uid] = self_beancount
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


class Transfer(Item):
    def __init__(
            self,
            source: str,
            destination: str,
            amount: Decimal,
            currency: str,
            date: datetime.date,
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
            date: datetime.date,
            notes: str = None,
    ) -> Transfer:
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
    def get_all(cls) -> List[Transfer]:
        return [
            Transfer.from_beancount(item)
            for item in physical_ledger.values()
            if item.meta["type"] == 'transfer'
        ]

    @classmethod
    def get(cls, uid: str) -> Transfer:
        return Transfer.from_beancount(physical_ledger.get(uid))

    def update(self,
               source: str,
               destination: str,
               amount: Decimal,
               currency: str,
               date: datetime.date,
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

    def commit(self):
        self_beancount = self.to_beancount()
        physical_ledger[self.uid] = self_beancount
        physical_ledger.commit()

    @classmethod
    def from_beancount(cls, item: Transaction) -> Transfer:
        source_posting = next((i for i in item.postings if i.units.number < 0))
        destination_posting = next((i for i in item.postings if i.units.number > 0))
        return Transfer(
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
                "type": "transfer",
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


class Income(Item):
    def __init__(
            self,
            source: str,
            destination: str,
            category: str,
            amount: Decimal,
            currency: str,
            date: datetime.date,
            physical_uid: str,
            logical_uid: str,
            notes: str = None,
    ):
        self.source = source
        self.destination = destination
        self.category = category
        self.amount = amount
        self.currency = currency
        self.date = date
        self.uid = physical_uid
        self.physical_uid = physical_uid
        self.logical_uid = logical_uid
        self.notes = notes

    @classmethod
    def create(
            cls,
            source: str,
            destination: str,
            category: str,
            amount: Decimal,
            currency: str,
            date: datetime.date,
            notes: str = None,
    ) -> Income:
        item = cls(
            source=source,
            destination=destination,
            category=category,
            amount=amount,
            currency=currency,
            date=date,
            physical_uid=str(uuid4()),
            logical_uid=str(uuid4()),
            notes=notes,
        )
        item.commit()
        return item

    @classmethod
    def get_all(cls) -> List[Income]:
        physical_entries = {
            item.meta["uid"]: item
            for item in physical_ledger.values()
            if item.meta["type"] == 'transfer'
        }
        logical_entries = {
            item.meta["physical_uid"]: item
            for item in logical_ledger.values()
            if item.meta["type"] == 'transfer'
        }
        return [
            Income.from_beancount(physical_entries[physical_uid], logical_entries[physical_uid])
            for physical_uid in physical_entries
        ]

    @classmethod
    def get(cls, uid: str) -> Optional[Income]:
        physical_entry = physical_ledger.get(uid)
        logical_entry = logical_ledger.get(physical_entry.meta["logical_uid"])
        if not physical_entry or not logical_entry:
            return None
        else:
            return Income.from_beancount(physical_entry, logical_entry)

    def update(self,
               source: str,
               destination: str,
               category: str,
               amount: Decimal,
               currency: str,
               date: datetime.date,
               physical_uid: str,
               logical_uid: str,
               notes: str = None,
               ) -> None:
        self.source = source
        self.destination = destination
        self.category = category
        self.amount = amount
        self.currency = currency
        self.date = date
        self.uid = physical_uid
        self.physical_uid = physical_uid
        self.logical_uid = logical_uid
        self.notes = notes
        self.commit()

    def delete(self) -> None:
        pass

    def commit(self):
        physical_ledger[self.physical_uid], logical_ledger[self.logical_uid] = self.to_beancount()
        physical_ledger.commit()
        logical_ledger.commit()

    @classmethod
    def from_beancount(cls, physical_item: Transaction, logical_item: Transaction) -> Income:
        source_posting = next((i for i in physical_item.postings if i.units.number < 0))
        destination_posting = next((i for i in physical_item.postings if i.units.number > 0))
        category_posting = next((i for i in logical_item.postings if i.units.number < 0))
        return Income(
            source=source_posting.account,
            destination=destination_posting.account,
            category=category_posting.account,
            amount=destination_posting.units.number,
            currency=destination_posting.units.currency,
            date=physical_item.date,
            physical_uid=physical_item.meta["uid"],
            logical_uid=logical_item.meta["uid"],
            notes=physical_item.narration,
        )

    def to_beancount(self) -> Tuple[Transaction, Transaction]:
        physical_entry = Transaction(
            meta={
                "uid": self.physical_uid,
                "type": "transfer",
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
        logical_entry = Transaction(
            meta={
                "uid": self.logical_uid,
                "type": "transfer",
            },
            date=self.date,
            flag="*",
            narration=self.notes,
            postings=[
                Posting(
                    account=self.category,
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
        return physical_entry, logical_entry
