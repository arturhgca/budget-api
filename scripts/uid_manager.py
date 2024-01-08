from io import StringIO
from uuid import uuid4

from beancount.loader import load_file
from beancount.scripts.format import align_beancount

from budget.ledger import monkeypatch


def add_uid(entry_type: str) -> None:
    items, _, _ = load_file(f"../beancountfiles/{entry_type}.beancount")
    for item in items:
        item.meta["uid"] = str(uuid4())
    items = sorted(items, key=lambda x: x.date)

    contents = StringIO()
    contents.writelines([f"{item}\n\n" for item in items])
    formatted = align_beancount(contents.getvalue())
    with open(f"../beancountfiles/{entry_type}.beancount", "w", encoding='UTF-8') as f:
        f.write(formatted)


add_uid("accounts")
add_uid("categories")
add_uid("currencies")
add_uid("sinks")
add_uid("sources")
