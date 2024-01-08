from datetime import datetime
from decimal import Decimal
from typing import List

from budget.facts import Allocation, Transfer


def create_transfer(
        source: str,
        destination: str,
        amount: Decimal,
        currency: str,
        date: str,
        notes: str = None,
) -> dict:
    return Transfer.create(
        source=source,
        destination=destination,
        amount=amount,
        currency=currency,
        date=datetime.strptime(date, "%Y-%m-%d"),
        notes=notes,
    ).as_dict()


def get_transfers() -> List[dict]:
    return [
        item.as_dict()
        for item in Transfer.get_all()
    ]


def get_transfer(uid: str) -> dict:
    return Transfer.get(uid=uid).as_dict()


def update_transfer(
        uid: str,
        source: str,
        destination: str,
        amount: Decimal,
        currency: str,
        date: str,
        notes: str = None,
) -> dict:
    transfer = Transfer.get(uid=uid)
    transfer.update(
        source=source,
        destination=destination,
        amount=amount,
        currency=currency,
        date=datetime.strptime(date, "%Y-%m-%d"),
        notes=notes,
    )
    return transfer.as_dict()


def delete_transfer(uid: str) -> dict:
    transfer = Transfer.get(uid=uid)
    contents = transfer.as_dict()
    transfer.delete()
    return contents
