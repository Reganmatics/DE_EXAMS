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
to clone the Repo
copya and paste the code below;
```
git clone https://github.com/Reganmatics/DE_EXAMS.git
```

## How to run code
This project uses a virtual environment and the packages used can be installed using the command below
```
pip install -r requirements.txt
```
OR
```
pip3 install -r requirements.txt
```

Next, we walk through the implemenations

we use the PostgresSQL DB to implement the ```ExpenseDatabase``` class methods
for this project, the credential used are

dbname = "metaverse",<br>
user = "cryptoverse_admin",<br>
host = "localhost",<br>
password = "admin",<br>
port = 5432

```
psql -h localhost -U cryptoverse_admin -d metaverse -p 5432 -W
```
This command breaks down as follows:

- <strong>-h localhost:</strong> Specifies the host (replace with your actual host if it's different).
- <strong>-U cryptoverse_admin:</strong> Specifies the username (replace with your actual username).
- <strong>-d metaverse:</strong> Specifies the database name (replace with your actual database name).
- <strong>-p 5432:</strong> Specifies the port number (replace with your actual port if it's different).
- <strong>-W:</strong> Prompts for the password.

After entering this command, you'll be prompted to enter the password for the specified user. Once you provide the correct password, you should be connected to the PostgreSQL database.

 we connect to the postgres server to verify our `ExpenseDatabase` methods.

We use the `psycopg` module to connect to the postgresql database from python.
#### Project Setup
1. Clone the project
2. navigate to the project directory
```
cd DE_EXAMS
```
3. install all packages used in project.
```
pip install -r requirements.txt
```
4. modify content of `expense_app.py` with your database credentials
5. run the main.py 
```
./main.py
```

feel free to modify the content of main.py to suit your needs