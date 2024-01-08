from collections import UserDict
from io import StringIO

from beancount.core.data import Transaction, Open, Commodity
from beancount.loader import load_file
from beancount.scripts.format import align_beancount

from . import monkeypatch


class Ledger(UserDict):
    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.options_map = None
        self._load()

    def _load(self):
        _entries, errors, self.options_map = load_file(filename=self.path)
        entries = {
            entry.meta["uid"]: entry for entry in _entries
            if 'uid' in entry.meta
               and "type" in entry.meta
        }
        transactions = {
            uid: entry for uid, entry in entries.items()
            if isinstance(entry, Transaction)
        }
        accounts = {
            uid: entry for uid, entry in entries.items()
            if isinstance(entry, Open)
        }
        commodities = {
            uid: entry for uid, entry in entries.items()
            if isinstance(entry, Commodity)
        }
        self.update(transactions)
        self.update(accounts)
        self.update(commodities)
        self.commit()

    def commit(self):
        contents = StringIO()
        contents.writelines([f"{item}\n\n" for item in sorted(self.values(), key=lambda x: x.date)])
        formatted = align_beancount(contents.getvalue())
        with open(f"{self.path}", "w", encoding='UTF-8') as f:
            f.write(formatted)
