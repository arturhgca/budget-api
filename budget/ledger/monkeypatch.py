from beancount.core.data import Transaction


def monkeypatch_transaction_str(self) -> str:
    postings = "\n".join([
        f"  {posting.account} {posting.units.number} {posting.units.currency}"
        for posting in self.postings
    ])
    return (
        f"{self.date.strftime('%Y-%m-%d')} * \"{self.narration}\""
        f"\n  type: \"{self.meta['type']}\""
        f"\n  uid: \"{self.meta['uid']}\""
        f"\n{postings}"
        f"\n"
    )


Transaction.__str__ = monkeypatch_transaction_str
