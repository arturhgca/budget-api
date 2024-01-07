from decimal import Decimal
from typing import List


def create_exchange(
    source: str,
    destination: str,
    source_amount: Decimal,
    destination_amount: Decimal,
    category: str,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


def get_exchanges() -> List[dict]:
    raise NotImplementedError


def get_exchange(uid: str) -> dict:
    raise NotImplementedError


def update_exchange(
    uid: str,
    source: str,
    destination: str,
    source_amount: Decimal,
    destination_amount: Decimal,
    category: str,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


def delete_exchange(uid: str) -> dict:
    raise NotImplementedError
