#!/usr/bin/env python3
from expense_app import Expense, ExpenseDatabase

def main_expense():
    """
    Parameters:
        No parameters are expected.

    Returns:
        No return value.
    """
    # define expense instance
    print("initialisation\n")
    exp1 = Expense('data', 100000)
    print(exp1.to_dict())
    # test for update by title
    print("\nTest for title upate\n")
    exp1.update(title = '1TB')
    print(exp1.to_dict())
    # test for update by amount
    print("\nTest for amount update\n")
    exp1.update(amount = 105000)
    print(exp1.to_dict())
    return list(item for item in exp1.to_dict().values())


def main_DB():
    exp1 = Expense('data', 100000)
    exp2 = Expense('tuition', 120000.50)
    db1 = ExpenseDatabase([exp1, exp2])
    #db1.add_expense(exp1)
    #db1.add_expense(exp2)
    # test for get expense by id
    print("\nTest for get expense by id\n")
    print(db1.get_expense_by_id(exp1.id))
    #test for get expense by title
    print("\nTest for get expense by title\n")
    print(db1.get_expense_by_title(exp2.title))
    # Test for remove_expense
    print("\nTest for remove expense\n")
    if db1.remove_expense('ff9a0206-5b8d-4d19-8186-3cf2bc0b2635'):
        print("Expense removed")
    
    print(db1.to_dict())   

if __name__ == "__main__":
    #print(f"{'='*13}TEST{'='*13}\n{'='*30}")
    #print(main_expense())
    print(f"{'='*30}\nmainDB Test\n{'='*30}")
    main_DB()