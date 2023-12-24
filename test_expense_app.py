#!/usr/bin/env python3
import unittest
from datetime import datetime
from expense_app import Expense, ExpenseDatabase

import unittest
from datetime import datetime, timezone
import uuid

class TestExpenseClass(unittest.TestCase):

    def test_init_method(self):
        title = "Test Expense"
        amount = 50.0
        expense = Expense(title, amount)

        # Check if id is a valid UUID
        self.assertTrue(uuid.UUID(expense.id))

        # Check if title and amount are assigned correctly
        self.assertEqual(expense.title, title)
        self.assertEqual(expense.amount, amount)

        # Check if created_at and updated_at are ISO formatted strings
        self.assertTrue(isinstance(expense.created_at, str))
        self.assertTrue(isinstance(expense.updated_at, str))

    def test_update_method(self):
        title = "Test Expense"
        amount = 50.0
        expense = Expense(title, amount)

        new_title = "Updated Expense"
        new_amount = 75.0

        # Update title and amount
        expense.update(title=new_title, amount=new_amount)

        # Check if title and amount are updated
        self.assertEqual(expense.title, new_title)
        self.assertEqual(expense.amount, new_amount)

        # Check if updated_at is modified
        self.assertNotEqual(expense.created_at, expense.updated_at)

    def test_to_dict_method(self):
        title = "Test Expense"
        amount = 50.0
        expense = Expense(title, amount)

        # Convert expense to dictionary
        expense_dict = expense.to_dict()

        # Check if the keys are present
        self.assertIn("id", expense_dict)
        self.assertIn("title", expense_dict)
        self.assertIn("amount", expense_dict)
        self.assertIn("created_at", expense_dict)
        self.assertIn("updated_at", expense_dict)

        # Check if the values are correct types
        self.assertTrue(isinstance(expense_dict["id"], str))
        self.assertTrue(isinstance(expense_dict["title"], str))
        self.assertTrue(isinstance(expense_dict["amount"], float))
        self.assertTrue(isinstance(expense_dict["created_at"], str))
        self.assertTrue(isinstance(expense_dict["updated_at"], str))


class TestExpenseDatabaseClass(unittest.TestCase):

    def setUp(self):
        # Create a test Expense object
        self.test_expense = Expense(title="Test Expense", amount=50.0)

        # Initialize an ExpenseDatabase with the test Expense
        self.expense_database = ExpenseDatabase([self.test_expense])

    def tearDown(self):
        # Close the database connection after each test
        self.expense_database.conn.close()

    def test_add_expense(self):
        # Add a new expense to the database
        new_expense = Expense(title="New Expense", amount=75.0)
        self.expense_database.add_expense(new_expense)

        # Retrieve the new expense by ID
        retrieved_expense = self.expense_database.get_expense_by_id(new_expense.id)

        # Check if the retrieved expense is the same as the added expense
        self.assertEqual(retrieved_expense, new_expense.to_dict())

    def test_remove_expense(self):
        # Remove the test expense from the database
        self.expense_database.remove_expense(self.test_expense.id)

        # Try to retrieve the removed expense by ID
        retrieved_expense = self.expense_database.get_expense_by_id(self.test_expense.id)

        # Check if the retrieved expense is None after removal
        self.assertIsNone(retrieved_expense)

    def test_get_expense_by_id(self):
        # Retrieve the test expense by ID
        retrieved_expense = self.expense_database.get_expense_by_id(self.test_expense.id)

        # Check if the retrieved expense is the same as the test expense
        self.assertEqual(retrieved_expense, self.test_expense.to_dict())

    def test_get_expense_by_title(self):
        # Retrieve expenses by title
        expenses_by_title = self.expense_database.get_expense_by_title("Test Expense")

        # Check if the test expense is in the list of retrieved expenses
        self.assertIn(self.test_expense.to_dict(), expenses_by_title)

    def test_to_dict(self):
        # Convert the database to a dictionary
        database_dict = self.expense_database.to_dict()

        # Check if the dictionary contains the correct keys
        self.assertIn("expenses", database_dict)

        # Check if the expenses key has the correct value
        self.assertEqual(database_dict["expenses"], [self.test_expense.to_dict()])

if __name__ == '__main__':
    unittest.main()
# Path: expense_app.py