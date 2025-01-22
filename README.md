# Finance-Tracker

Finance Tracker is a simple and intuitive tool to help you manage your expenses, stick to your budget, and get a better understanding of your spending habits. It gives you the flexibility to use a command-line interface (CLI) for quick inputs or a user-friendly web application for a more visual experience.

## Features

### CLI Features
- **Add Expenses**: Enter your expense details like name, category, and amount directly into the terminal.
- **Track Your Budget**: Keep an eye on your remaining budget and calculate how much you can spend daily.
- **Summary Reports**: Get a clear breakdown of your spending by category.

### Web Application Features
- **Easy-to-Use Interface**: Add and view your expenses in a visually appealing and straightforward web interface.
- **Visual Insights**: See your spending patterns in real-time with pie charts grouped by category.
- **Secure Storage**: All your expense data is saved in a CSV file for easy access and backup.

## Technologies Used
- **Programming Language**: Python
- **Web Framework**: Flask
- **Frontend**: HTML and Jinja2 templates
- **Storage**: CSV files for simple, accessible data storage
- **Libraries**:
  - `collections` for organizing and grouping data
  - `datetime` and `calendar` for date and budget calculations

## Project Structure

finance-tracker/
|-- app.py              # Flask web application
|-- expense.py          # Defines the Expense class
|-- expense_tracker.py  # CLI-based tracker
|-- expenses.csv        # Stores expense data
|-- templates/          # HTML templates for Flask
    |-- index.html      # Web application interface




