from collections import UserList

from beancount.loader import load_file
from beancount.query.query import run_query


class Ledger(UserList):
    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.options_map = None
        self._load()

    def _load(self):
        entries, errors, options_map = load_file(filename=self.path)
        self.extend(entries)
        self.options_map = options_map

    def get(self, uid: str) -> dict:
        rtypes, rrows = run_query(
            entries=self,
            options_map=self.options_map,
            query=f"SELECT * WHERE uid={uid}",
        )
        return rrows[0] if rrows else {}
