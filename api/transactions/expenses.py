from decimal import Decimal


def create_expense(
    account: str,
    sink: str,
    category: str,
    amount: Decimal,
    date: str,
    notes: str = None,
):
    raise NotImplementedError


def get_expenses():
    raise NotImplementedError


def get_expense(uid: str):
    raise NotImplementedError


def update_expense(
    uid: str,
    account: str,
    sink: str,
    category: str,
    amount: Decimal,
    date: str,
    notes: str = None,
):
    raise NotImplementedError


def delete_expense(uid: str):
    raise NotImplementedError
