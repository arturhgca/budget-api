from decimal import Decimal
from typing import List

import pendulum

from budget.facts import Allocation


def create_allocation(
    source: str,
    destination: str,
    amount: Decimal,
    currency: str,
    date: str,
    notes: str = None,
) -> dict:
    return Allocation.create(
        source=source,
        destination=destination,
        amount=amount,
        currency=currency,
        date=pendulum.from_format(date, fmt="%Y-%m-%d"),
        notes=notes,
    ).as_dict()


def get_allocations() -> List[dict]:
    return [
        item.as_dict()
        for item in Allocation.get_all()
    ]


def get_allocation(uid: str) -> dict:
    return Allocation.get(uid=uid).as_dict()


def update_allocation(
    uid: str,
    source: str,
    destination: str,
    amount: Decimal,
    currency: str,
    date: str,
    notes: str = None,
) -> dict:
    allocation = Allocation.get(uid=uid)
    allocation.update(
        source=source,
        destination=destination,
        amount=amount,
        currency=currency,
        date=pendulum.from_format(date, fmt="%Y-%m-%d"),
        notes=notes,
    )
    return allocation.as_dict()


def delete_allocation(uid: str) -> dict:
    allocation = Allocation.get(uid=uid)
    contents = allocation.as_dict()
    allocation.delete()
    return contents
