# Alt School Fall Semseter DE Exams Hands on Project

## Project Description
### Expense Class:
Represents an individual financial expense.

#### Attributes:

1. <strong>id:</strong> A unique identifier generated as a UUID string.
2. <strong>title:</strong> A string representing the title of the expense.
3. <strong>amount:</strong> A float representing the amount of the expense.
4. <strong>created_at:</strong> A timestamp indicating when the expense was created (UTC).
5. <strong>updated_at:</strong> A timestamp indicating the last time the expense was updated (UTC).

#### Methods:
1. <strong>__init__:</strong> Initializes the attributes.
2. <strong>update:</strong> Allows updating the title and/or amount, updating the updated_at timestamp.
3. <strong>to_dict:</strong> Returns a dictionary representation of the expense.

### ExpenseDB class
Manages a collection of Expense objects.

#### Attributes:

1. <strong>expenses:</strong> A list storing Expense instances.
#### Methods:

1. <strong>__init__:</strong> Initializes the list.
2. <strong>add_expense:</strong> Adds an expense.
3. <strong>remove_expense:</strong> Removes an expense.
4. <strong>get_expense_by_id:</strong> Retrieves an expense by ID.
5. <strong>get_expense_by_title:</strong> Retrieves expenses by title.
6. <strong>to_dict:</strong> Returns a list of dictionaries representing expenses.
## How to clone project


## How to run code