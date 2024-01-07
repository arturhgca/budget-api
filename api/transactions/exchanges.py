from decimal import Decimal


def create_exchange(
    source: str,
    destination: str,
    source_amount: Decimal,
    destination_amount: Decimal,
    category: str,
    date: str,
    notes: str = None,
):
    raise NotImplementedError


def get_exchanges():
    raise NotImplementedError


def get_exchange(uid: str):
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
):
    raise NotImplementedError


def delete_exchange(uid: str):
    raise NotImplementedError
