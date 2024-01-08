from io import StringIO
from typing import Dict, Any

from beancount.core.data import Transaction, Open, Commodity
from beancount.loader import load_file
from beancount.scripts.format import align_beancount

from . import monkeypatch


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

    def get(self, uid: str) -> Any:
        return self.entries[uid]

    def commit(self):
        contents = StringIO()
        contents.writelines([f"{item}\n\n" for item in self.entries.values()])
        formatted = align_beancount(contents.getvalue())
        with open(f"{self.path}2", "w", encoding='UTF-8') as f:
            f.write(formatted)
