import sqlite3

# Connect to SQLite database (this will create a new database if it doesn't exist)
connection = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the table schema with AUTOINCREMENT for the id column
create_table_query = '''
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Company TEXT,
    amount REAL,
    date_paid TEXT,
    status TEXT,
    due_date TEXT
);
'''

# Execute the create table query
cursor.execute(create_table_query)

# Insert data into the table
data = [
    ('derm', 4100.00, '2023-09-26', 'paid', '2024-01-15'),
    ('derm', 4100.00, '2023-10-12', 'paid', '2024-01-15'),
    ('tek', 15200.00, '2023-06-09', 'paid', '2023-06-15'),
    ('tek', 15200.00, '2023-07-12', 'paid', '2023-09-15'),
    ('tek', 11400.00, '2023-08-11', 'paid', '2023-09-15'),
    ('tek', 14440.00, '2023-09-21', 'paid', '2024-01-15'),
    ('tek', 15200.00, '2023-10-18', 'paid', '2024-01-15'),
    ('tek', 23520.00, None, 'unpaid', '2024-01-15'),  # Use None for NULL
    ('tek', 16800.00, None, 'unpaid', '2024-01-15'),
    ('tek', 16800.00, None, 'unpaid', '2024-01-15'),
    ('tek', 16800.00, None, 'unpaid', '2024-01-15')
]

# Insert data into the table
cursor.executemany('INSERT INTO my_table (Company, amount, date_paid, status, due_date) VALUES (?, ?, ?, ?, ?)', data)

# Commit the changes and close the connection
connection.commit()
connection.close()
