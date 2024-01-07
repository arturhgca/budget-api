from decimal import Decimal
from typing import List


def create_transfer(
    source: str, destination: str, amount: Decimal, date: str, notes: str = None
) -> dict:
    raise NotImplementedError


def get_transfers() -> List[dict]:
    raise NotImplementedError


def get_transfer(uid: str) -> dict:
    raise NotImplementedError


def update_transfer(
    uid: str,
    source: str,
    destination: str,
    amount: Decimal,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


def delete_transfer(uid: str) -> dict:
    raise NotImplementedError
