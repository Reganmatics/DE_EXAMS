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

if __name__ == '__main__':
    unittest.main()
