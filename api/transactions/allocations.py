from decimal import Decimal


def create_allocation(
    source: str,
    destination: str,
    amount: Decimal,
    currency: str,
    date: str,
    notes: str = None,
):
    raise NotImplementedError


def get_allocations():
    raise NotImplementedError


def get_allocation(uid: str):
    raise NotImplementedError


def update_allocation(
    uid: str,
    source: str,
    destination: str,
    amount: Decimal,
    currency: str,
    date: str,
    notes: str = None,
):
    raise NotImplementedError


def delete_allocation(uid: str):
    raise NotImplementedError
