from beancount.core.data import Transaction, Posting, Open, Close, Commodity


def monkeypatch_transaction_str(self: Transaction) -> str:
    headline = f"{self.date.strftime('%Y-%m-%d')} {self.flag}"
    if self.narration:
        headline += f' "{self.narration}"'
    meta = [
        f"\n  type: \"{self.meta['type']}\""
        f"\n  uid: \"{self.meta['uid']}\""
    ]
    postings = [
        f"\n  {posting}"
        for posting in self.postings
    ]
    return headline + ''.join(meta) + ''.join(postings)


def monkeypatch_posting_str(self: Posting) -> str:
    line = f"{self.account} {self.units.number} {self.units.currency}"
    if self.cost:
        line += f" @@ {self.cost.number} {self.cost.currency}"
    elif self.price:
        line += f" @ {self.price.number} {self.price.currency}"
    return line


def monkeypatch_open_str(self: Open) -> str:
    headline = f"{self.date.strftime('%Y-%m-%d')} open {self.account}"
    meta = [
        f"\n  type: \"{self.meta['type']}\""
        f"\n  uid: \"{self.meta['uid']}\""
    ]
    return headline + ''.join(meta)


def monkeypatch_close_str(self: Close) -> str:
    headline = f"{self.date.strftime('%Y-%m-%d')} close {self.account}"
    meta = [
        f"\n  type: \"{self.meta['type']}\""
        f"\n  uid: \"{self.meta['uid']}\""
    ]
    return headline + ''.join(meta)


def monkeypatch_commodity_str(self: Commodity) -> str:
    headline = f"{self.date.strftime('%Y-%m-%d')} commodity {self.currency}"
    meta = [
        f"\n  type: \"{self.meta['type']}\""
        f"\n  uid: \"{self.meta['uid']}\""
    ]
    if self.meta.get("price"):
        meta.append(
            f"\n  price: \"{self.meta['price']}\""
        )
    return headline + ''.join(meta)


Transaction.__str__ = monkeypatch_transaction_str
Posting.__str__ = monkeypatch_posting_str
Open.__str__ = monkeypatch_open_str
Close.__str__ = monkeypatch_close_str
Commodity.__str__ = monkeypatch_commodity_str
