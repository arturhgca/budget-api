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
    ).as_dict


def get_allocations() -> List[dict]:
    raise NotImplementedError


def get_allocation(uid: str) -> dict:
    raise NotImplementedError


def update_allocation(
    uid: str,
    source: str,
    destination: str,
    amount: Decimal,
    currency: str,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


def delete_allocation(uid: str) -> dict:
    raise NotImplementedError
