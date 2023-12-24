#!/usr/bin/env python3
"""AltSchool DE Exams: hands on project
"""

import psycopg
import uuid
from datetime import datetime, timezone
import uuid

class Expense:
    """Represents an individual financial expense.
    """

    def __init__(self, title, amount):
        """class init function
        """
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc).isoformat() #.strftime('%Y-%m-%d %H:%M:%S.%f%z')
        self.updated_at = self.created_at

    def update(self, title = None, amount = None):
        """
        Allows updating the title and/or amount, updating the 
        updated_at timestamp.
        """
        if title is not None:
            self.title = title
        
        if amount is not None:
            self.amount = amount
        self.updated_at = datetime.now(timezone.utc).isoformat() #.strftime('%Y-%m-%d %H:%M:%S.%f%z') #self._timezone()

    def to_dict(self):
        "Returns a dictionary representation of the expense."
        
        return {
                "id": str(self.id),
                "title": self.title,
                "amount": self.amount,
                "created_at": self.created_at,
                "updated_at": self.updated_at
                }
    
    def _timezone(self):
        return datetime.utcnow().astimezone()

class ExpenseDatabase:
    """Manages a collection of Expense objects.
    """

    def __init__(self):
        """Initializes the list.
        """
        self.expenses = []
        # to recreate the analysis withput errors, make sure to edit the connection parameters below
        self.conn = psycopg.connect(dbname = "metaverse",
                        user = "cryptoverse_admin",
                        host = "localhost",
                        password = "admin",
                        port = 5432)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS budget (
                id UUID PRIMARY KEY,
                title VARCHAR(255),
                amount NUMERIC,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
                """)
        self.conn.commit()

    def add_expense(self, expense):
        """Adds an expense.
        """
        query = """
            INSERT INTO budget (id, title, amount, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s);
                """
        self.cur.execute(query, (str(expense.id), expense.title, expense.amount, expense.created_at, expense.updated_at))
        self.conn.commit()

    def remove_expense(self, expense_id):
        """Removes an expense.
        """
        self.cur.execute("""
        DELETE FROM budget
        WHERE id = %s;
        """, (expense_id,))
        self.conn.commit()

    def get_expense_by_id(self, expense_id):
        """Retrieves an expense by ID.
        """
        self.cur.execute("""
        SELECT 
            * 
        FROM
            budget
        WHERE id = %s;
        """, (expense_id,))
        
        result = self.cur.fetchone()
        return result

    def get_expense_by_title(self, expense_title):
        """Retrieves expenses by title.
        """
        self.cur.execute("""
        SELECT 
                * 
        FROM
                budget
        WHERE title=%s;
        """, (expense_title,))
        result = self.cur.fetchall()
        return [item for item in result]
    
    def to_dict(self):
        """Returns a list of dictionaries representing expenses.
        """
        return {
            "expenses": [expense.to_dict() for expense in self.expenses]
        }

    def close(self):
        """close the database connection.
        """
        self.cur.close()
        self.conn.close()

