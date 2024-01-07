from decimal import Decimal
from typing import List


def create_expense(
    account: str,
    sink: str,
    category: str,
    amount: Decimal,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


def get_expenses() -> List[dict]:
    raise NotImplementedError


def get_expense(uid: str) -> dict:
    raise NotImplementedError


def update_expense(
    uid: str,
    account: str,
    sink: str,
    category: str,
    amount: Decimal,
    date: str,
    notes: str = None,
) -> dict:
    raise NotImplementedError


def delete_expense(uid: str) -> dict:
    raise NotImplementedError
