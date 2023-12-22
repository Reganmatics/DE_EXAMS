#!/usr/bin/env python3
"""AltSchool DE Exams: hands on project
"""

import psycopg
import uuid
from datetime import datetime, timezone

class Expense:
    """Represents an individual financial expense.
    """

    def __init__(self, title, amount):
        """class init function
        """
        self.id = uuid.uuid4()
        self.title = title
        self.amount = amount
        self.created_at = datetime.now(timezone.utc)
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
        self.updated_at = self._timezone()

    def to_dict(self):
        "Returns a dictionary representation of the expense."
        
        return {
                "id": self.id,
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

    def __init__(self, expenses):
        """Initializes the list.
        """
        self.expenses = []
        self.conn = psycopg.connect(dbname = "metaverse",
                        user = "cryptoverse_admin",
                        host = "localhost",
                        password = "admin",
                        port = 5432)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS budget (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                amount NUMERIC,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
                """)
        self.conn.commit()

    def test(self):
        result = self.cur.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = 'public'
            AND table_name='budget';
            """)

        # Make the changes to the database persistent
        # self.conn.commit()
        return [item for item in result]

    def add_expense(self, expense):
        """Adds an expense.
        """
        self.cur.execute(f"""
            INSERT INTO budget (title, amount, created_at, updated_at)
            VALUES
                {expense.values()}
                """)
        self.conn.commit()
        

    def remove_expense(self, expense_id):
        """Removes an expense.
        """
        self.cur.execute("""
                """)
        self.conn.commit()
        pass

    def get_expense_by_id(self, expense_id):
        """Retrieves an expense by ID.
        """
        result = self.cur.execute(f"""
        SELECT 
                * 
        FROM
                Budget
        WHERE id={expense_id};
                """)
        return [item for item in result]

    def get_expense_by_title(self, expense_title):
        """Retrieves expenses by title.
        """
        result = self.cur.execute(f"""
        SELECT 
                * 
        FROM
                Budget
        WHERE title={expense_title};
                """)
        return [item for item in result]

    def close(self):
        """close the database connection.
        """
        self.cur.close()
        self.conn.close()

def main_expense():
    """
    Parameters:
        No parameters are expected.

    Returns:
        No return value.
    """
    exp1 = Expense('data', 100000)
    #exp2 = Expense('')
    #exp1.update(amount = 105000)
    exp1.update(title = '1TB')
    return list(item for item in exp1.to_dict().values())

def main_DB():
    exp1 = Expense('data', 100000)
    db1 = ExpenseDatabase(exp1)
    print(db1.add_expense)

if __name__ == "__main__":
    #print(main_DB())
    print(main_expense())