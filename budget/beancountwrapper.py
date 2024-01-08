from io import StringIO
from typing import Any, Dict

from beancount.core.data import Transaction, Open, Commodity
from beancount.loader import load_file
from beancount.scripts.format import align_beancount


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


class Ledger:
    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.options_map = None
        self.entries: Dict[str, Any] = dict()
        self.transactions: Dict[str, Transaction] = dict()
        self.accounts: Dict[str, Open] = dict()
        self.commodities: Dict[str, Commodity] = dict()
        self._load()

    def _load(self):
        _entries, errors, self.options_map = load_file(filename=self.path)
        entries = {
            entry.meta["uid"]: entry for entry in _entries
            if 'uid' in entry.meta
               and "type" in entry.meta
        }
        self.transactions = {
            uid: entry for uid, entry in entries.items()
            if isinstance(entry, Transaction)
        }
        self.accounts = {
            uid: entry for uid, entry in entries.items()
            if isinstance(entry, Open)
        }
        self.commodities = {
            uid: entry for uid, entry in entries.items()
            if isinstance(entry, Commodity)
        }
        self.entries.update(self.transactions)
        self.entries.update(self.accounts)
        self.entries.update(self.commodities)
        self.commit()

    def get(self, uid: str) -> Any:
        return self.entries[uid]

    def commit(self):
        contents = StringIO()
        contents.writelines([f"{item}\n" for item in self.entries.values()])
        formatted = align_beancount(contents.getvalue())
        with open(f"{self.path}", "w", encoding='UTF-8') as f:
            f.write(formatted)
