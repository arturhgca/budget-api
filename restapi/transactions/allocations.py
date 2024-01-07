from decimal import Decimal
from typing import List


def create_allocation(
    source: str,
    destination: str,
    amount: Decimal,
    currency: str,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


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
