from flask import Flask, render_template, request, redirect, url_for, jsonify
from expense import Expense
from collections import defaultdict

app = Flask(__name__)

# Initialize an empty list to store expenses
expenses = []

@app.route("/", methods=["GET", "POST"])
def home():
    global expenses
    if request.method == "POST":
        expense_name = request.form.get("expense_name")
        expense_amount = float(request.form.get("expense_amount"))
        expense_category = request.form.get("expense_category")

        # Create an Expense object and add it to the list
        new_expense = Expense(name=expense_name, amount=expense_amount, category=expense_category)
        expenses.append(new_expense)

        return redirect(url_for("home"))

    return render_template("index.html", expenses=expenses)


@app.route("/chart-data")
def chart_data():
    """Provide data for pie chart."""
    # Group expenses by category
    category_totals = defaultdict(float)
    for expense in expenses:
        category_totals[expense.category] += expense.amount

    # Prepare data for pie chart
    pie_chart_data = {
        "labels": list(category_totals.keys()),
        "data": list(category_totals.values()),
    }

    return jsonify(pie_chart_data)


if __name__ == "__main__":
    app.run(debug=True)
