from decimal import Decimal
from typing import List


def create_income(
    source: str, account: str, amount: Decimal, date: str, notes: str = None
) -> dict:
    raise NotImplementedError


def get_incomes() -> List[dict]:
    raise NotImplementedError


def get_income(uid: str) -> dict:
    raise NotImplementedError


def update_income(
    uid: str, source: str, account: str, amount: Decimal, date: str, notes: str = None
) -> dict:
    raise NotImplementedError


def delete_income(uid: str) -> dict:
    raise NotImplementedError
