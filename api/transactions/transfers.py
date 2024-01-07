from decimal import Decimal


def create_transfer(
    source: str, destination: str, amount: Decimal, date: str, notes: str = None
):
    raise NotImplementedError


def get_transfers():
    raise NotImplementedError


def get_transfer(uid: str):
    raise NotImplementedError


def update_transfer(
    uid: str,
    source: str,
    destination: str,
    amount: Decimal,
    date: str,
    notes: str = None,
):
    raise NotImplementedError


def delete_transfer(uid: str):
    raise NotImplementedError
