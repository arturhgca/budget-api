from decimal import Decimal


def create_income(
    source: str, account: str, amount: Decimal, date: str, notes: str = None
):
    raise NotImplementedError


def get_incomes():
    raise NotImplementedError


def get_income(uid: str):
    raise NotImplementedError


def update_income(
    uid: str, source: str, account: str, amount: Decimal, date: str, notes: str = None
):
    raise NotImplementedError


def delete_income(uid: str):
    raise NotImplementedError
