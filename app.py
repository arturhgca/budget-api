from flask import Flask
from restapi import transactions

app = Flask(__name__)

app.add_url_rule(
    "/transactions/allocations",
    methods=["POST"],
    view_func=transactions.allocations.create_allocation,
)
app.add_url_rule(
    "/transactions/allocations",
    methods=["GET"],
    view_func=transactions.allocations.get_allocations,
)
app.add_url_rule(
    "/transactions/allocations/${uid}",
    methods=["GET"],
    view_func=transactions.allocations.get_allocation,
)
app.add_url_rule(
    "/transactions/allocations/${uid}",
    methods=["PUT"],
    view_func=transactions.allocations.update_allocation,
)
app.add_url_rule(
    "/transactions/allocations/${uid}",
    methods=["DELETE"],
    view_func=transactions.allocations.delete_allocation,
)

app.add_url_rule(
    "/transactions/exchanges",
    methods=["POST"],
    view_func=transactions.exchanges.create_exchange,
)
app.add_url_rule(
    "/transactions/exchanges",
    methods=["GET"],
    view_func=transactions.exchanges.get_exchanges,
)
app.add_url_rule(
    "/transactions/exchanges/${uid}",
    methods=["GET"],
    view_func=transactions.exchanges.get_exchange,
)
app.add_url_rule(
    "/transactions/exchanges/${uid}",
    methods=["PUT"],
    view_func=transactions.exchanges.update_exchange,
)
app.add_url_rule(
    "/transactions/exchanges/${uid}",
    methods=["DELETE"],
    view_func=transactions.exchanges.delete_exchange,
)

app.add_url_rule(
    "/transactions/expenses",
    methods=["POST"],
    view_func=transactions.expenses.create_expense,
)
app.add_url_rule(
    "/transactions/expenses",
    methods=["GET"],
    view_func=transactions.expenses.get_expenses,
)
app.add_url_rule(
    "/transactions/expenses/${uid}",
    methods=["GET"],
    view_func=transactions.expenses.get_expense,
)
app.add_url_rule(
    "/transactions/expenses/${uid}",
    methods=["PUT"],
    view_func=transactions.expenses.update_expense,
)
app.add_url_rule(
    "/transactions/expenses/${uid}",
    methods=["DELETE"],
    view_func=transactions.expenses.delete_expense,
)

app.add_url_rule(
    "/transactions/incomes",
    methods=["POST"],
    view_func=transactions.incomes.create_income,
)
app.add_url_rule(
    "/transactions/incomes", methods=["GET"], view_func=transactions.incomes.get_incomes
)
app.add_url_rule(
    "/transactions/incomes/${uid}",
    methods=["GET"],
    view_func=transactions.incomes.get_income,
)
app.add_url_rule(
    "/transactions/incomes/${uid}",
    methods=["PUT"],
    view_func=transactions.incomes.update_income,
)
app.add_url_rule(
    "/transactions/incomes/${uid}",
    methods=["DELETE"],
    view_func=transactions.incomes.delete_income,
)

app.add_url_rule(
    "/transactions/transfers",
    methods=["POST"],
    view_func=transactions.transfers.create_transfer,
)
app.add_url_rule(
    "/transactions/transfers",
    methods=["GET"],
    view_func=transactions.transfers.get_transfers,
)
app.add_url_rule(
    "/transactions/transfers/${uid}",
    methods=["GET"],
    view_func=transactions.transfers.get_transfer,
)
app.add_url_rule(
    "/transactions/transfers/${uid}",
    methods=["PUT"],
    view_func=transactions.transfers.update_transfer,
)
app.add_url_rule(
    "/transactions/transfers/${uid}",
    methods=["DELETE"],
    view_func=transactions.transfers.delete_transfer,
)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
