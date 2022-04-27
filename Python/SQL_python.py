#### Python SQL libraries

#There are a multitude of SQL libraries available for Python

 SQLite (sqlite3)
 MySQL (mysql-connectorpython)
 PostgreSQL (psycopg2)
 PyPi (python-sql)
 SQLAlchemy
 Records
 PugSQL
 DjangoORM
 Peewee
 PonyORM
 SQLOBject

 The main job of these libraries is to give you access to a
way to communicate with your database
 This is done by creating connections to the server of your
database or in some cases to the database on your hard
drive
 Than you hand over (non-)standard SQL queries to the
connection so that they can be executed
 Therefore it‘s more important to remember the corrrect SQL
syntax.

#### SQLite

 We will use SQLlite since it‘s an offline version of SQL and
allows us to work on the databases directly on our
harddrive
 It uses a nonstandard variant of the SQL query language


import sqlite3


#### Connect to your database

 To start working with SQLlite you have to first connect to
your database
 This principle is the same for other SQL libraries as well,
but this time we don‘t have to set up a server connection
 If the database doesn‘t exist it will be created on the spot
    import sqlite3
    con = sqlite3.connect('example.db')

#### The Cursor object

 Once you have established the connection to your
database you have to create a cursor object
 This object can than help you modify your database with
the help of it‘s execute() method to perform SQL commands
 Syntax:
 cur = con.cursor()



# cur = db.cursor()


#### Creating tables

 To create tables we need to use the execute method of our
cursor object
 Than we can use a syntax similiar to the one of SQL we
saw earlier
 cur.execute('''CREATE TABLE stocks (date text,
trans text, symbol text, qty real, price real)''')
 Don‘t forget to save (commit) your changes once you‘re
done
 con.commit(

# cur.execute('''CREATE TABLE decks (Short varchar(255), Colors varchar(255), FullName varchar(255), Price real, Wins int)''')
# cur.execute("INSERT INTO decks VALUES ('Arix','UG','Arixmethes, the Slumbering Isle',450.28,5)")
# for row in cur.execute('SELECT * FROM decks'):
#     print(row)

# real data type for float variables

#### Datatypes in SQLlite

 SQLlite allows each column in a table to be one of the
following data types:
 NULL: The value is a NULL value.
 INTEGER: The value is a signed integer
 REAL: The value is a floating point value
 TEXT: The value is a text string
 BLOB: The value is a blob of data, stored exactly as it was input

#### Closing your database

 You can close the connection to your database if you‘re
done with it
 Syntax:
# con.close()

#### Your database

 By now your database should include three tables
 Two of them should have somewhat around 6 to 8 columns
and contain CHECKs, PRIMARY KEYs,
AUTO_INCREMENTs, NOT NULLs and DEFAULTs
 The third should have somewhat around 4 to 6 columns
and contain two FOREIGN KEYs from the other two tables
 If your database differs from that, please let me know, so
that you can change it
 We need this database for our exercises about queries as
we go on

#### Exercise 35 - Python Database

# Use the sqllite module of Python to create your first databases
# The database should have at least seven tables
# Some of them should have 6 to 10 columns and the other ones 2 to 4 columns

import sqlite3

db = sqlite3.connect("DatabaseCQ.db")
cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS samplers")
cur.execute("DROP TABLE IF EXISTS keyboards")
cur.execute("DROP TABLE IF EXISTS speakers")
cur.execute("DROP TABLE IF EXISTS synths")
cur.execute("DROP TABLE IF EXISTS order_history")
cur.execute("DROP TABLE IF EXISTS vinyl")
cur.execute("DROP TABLE IF EXISTS accessories")

cur.execute(
    """CREATE TABLE samplers (id INTEGER primary key AUTOINCREMENT, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE keyboards (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE speakers (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE synths (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE order_history (order_id integer NOT NULL primary key autoincrement, Item, Item_id, Date Ordered, Delivery Status, Orders)"""
)

cur.execute(
    """CREATE TABLE accessories (id integer NOT NULL primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE useless (id integer NOT NULL primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

db.commit()
db.close()

#### Filling your Tables [4]

#  Now we can add data to our tables
#  Just like we saw for SQL we have to use the INSERT INTO
# command
#  Syntax:
#
#  cur.execute("INSERT INTO stocks VALUES ('2006-01-
# 05','BUY','RHAT',100,35.14)"

#### Exercise 36 – Filling your database

#  It’s time to put data into your tables
#  Fill at least three of your tables from Exercise 35 with at
# least 10 rows of data
#  Keep in mind that you don’t have to create the tables again

print(samplers)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('SP404','Roland', '$899','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('SP404SX','Roland', '$499','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('SP404A','Roland', '$399','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('SP404MKII','Roland', '$499','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock)VALUES ('MPC1000','AKAI', '$300','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock)VALUES ('MPC2000XL','AKAI', '$3400','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock)VALUES ('MPCLIVE','AKAI', '$1000','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('MPCX','AKAI', '$1200','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('PO33','Teenage Engineering', '$99','12')"
)
cur.execute(
    "INSERT INTO samplers (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('PO32','Teenage Engineering', '$79','12')"
)
for row in cur.execute("SELECT * FROM samplers"):
    print(row)

print(keyboards)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('PSR-E373','Yamaha', '$219','3')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('CT-S1000V','Casio', '$475','6')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('PSR-SX700','Yamaha', '$1089','18')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('CT-S500','Casio', '$399','8')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('SP-5600','Thomann', '$398','14')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock)VALUES ('MKR 61','Startone', '$46','11')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('CT-S400','Casio', '$240','3')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('AK-X1100','Thomann', '$599','12')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('CT-S1WE','Casio', '$235','9')"
)
cur.execute(
    "INSERT INTO keyboards (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('LK-S450','Casio', '$295','12')"
)
for row in cur.execute("SELECT * FROM keyboards"):
    print(row)

print(Synths)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('Matriarch','Moog', '$1945','3')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('MPK mimi Play MK3','AKAI', '$125','6')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('Poly D','Behringer', '$625','18')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('MonoPoly','Behringer', '$535','8')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('Prophet REV2-8','Sequential', '$1579','14')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('DeepMind 12','Behringer', '$725','11')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('MiniBrute 2 Noir','Arturia', '$489','3')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('Minilogue XD','Korg', '$539','12')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('MODX8','Yamaha', '$1599','9')"
)
cur.execute(
    "INSERT INTO synths (Name, Manufacturer, Price, Quantity_In_Stock) VALUES ('PolyBrute','Arturia', '$2399','12')"
)
for row in cur.execute("SELECT * FROM synths"):
    print(row)


#### Deleting tables

You can delete tables by simply using the DROP TABLE
command as we saw in SQL
 Example:
 cur.execute("DROP TABLE emp")

 You can combine the DROP TABLE method with the IF
EXISTS method to drop tables only if they are already there

cur.execute('DROP TABLE IF EXISTS department')

Exercise 37 – Deleting Tables

#Delete at least three of your tables from Exercise 35

cur.execute("DROP TABLE useless")

#### Altering Tables [7]

#  There are two ways to alter your tables
#  The first one is to rename one of your tables
#  Example:

#  renameTable = "ALTER TABLE stud RENAME TO student"
#  cursor.execute(renameTable)
#
# The second way is to add columns to your tables

#  Examples:
#  addColumn = "ALTER TABLE teacher ADD COLUMN
# Address text"
#  cur.execute(addColumn)
#
#  Unfortunately it‘s not easy to drop columns from tables with
# SQLlite
#  You have to create a new table with data from the old one
# you want to keep and than remove the old table bevor
# renaming the new table

# Syntax:
# CREATE TABLE t1_backup AS SELECT a, b FROM t1;
# DROP TABLE t1;
# ALTER TABLE t1_backup RENAME TO t1;


#### Exercise 38 - Altering tables

# 1. Add at least three columns to each of your old tables
# 2. Create two new tables from your existing tables with the
# help of CREATE TABLE and SELECT
# 3. Rename at least two tables


#1.
#
# AddColumn = "ALTER TABLE vinyl ADD COLUMN monkeys"
# cur.execute(addColumn)
#
# AddColumn = "ALTER TABLE vinyl ADD COLUMN elephants"
# cur.execute(addColumn)
#
# AddColumn = "ALTER TABLE vinyl ADD COLUMN lions"
# cur.execute(addColumn)

#2.



renameTable = "ALTER TABLE samplers RENAME TO Samplers"
cursor.execute(renameTable)

AddColumn = "ALTER TABLE Order ADD COLUMN Address text"
cur.execute(addColumn)

cur.execute(
    """CREATE TABLE vinyl (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

### Constraints

 SQLite supports different Constraints:
 PRIMARY KEY
 NOT NULL
 UNIQUE
 FOREIGN KEY
 DEFAULT
 CHECK
 The concepts of these constraints should be known to you by now

 PRIMARY KEY:
 column_1 NOT NULL DATATYPE PRIMARY KEY
 column_1 NOT NULL DATATYPE,
 column_2 NOT NULL DATATYPE,
 ...  PRIMARY KEY(column_1, column_2,…)

 FOREIGN KEY:
 FOREIGN KEY (column_name) REFERENCES table2_name
(column_2_name)
 NOT NULL:
 column_name dataType NOT NULL
 DEFAULT:
 column_name dataType DEFAULT DEFAULT_VALUE
 CHECK:
 column_name dataType CHECK(condition)

cur.execute("""CREATE TABLE department
( name TEXT NOT NULL,
deptno INTEGER NOT NULL PRIMARY KEY)""")
ur.execute("""CREATE TABLE employee
(name TEXT NOT NULL,
ssn TEXT NOT NULL PRIMARY KEY,
bdate TEXT,
address TEXT,
salary INTEGER CHECK(salary > 1000),
dno INTEGER NOT NULL,
FOREIGN KEY (dno) REFERENCES department (deptno))""")

cur.execute("""CREATE TABLE deptlocations
(dnumber INTEGER NOT NULL,
dlocation TEXT NOT NULL,
PRIMARY KEY (dnumber, dlocation),
FOREIGN KEY (dnumber) REFERENCES department (deptno))""")
cur.execute("""CREATE TABLE project
(pname TEXT NOT NULL,
pnumber INTEGER NOT NULL,
plocation TEXT NOT NULL,
dnum INTEGER NOT NULL,
PRIMARY KEY (pnumber, plocation),
FOREIGN KEY (dnum) REFERENCES department (deptno))""")

cur.execute("""CREATE TABLE works_on
(essn TEXT NOT NULL,
pno INTEGER NOT NULL,
hour INTEGER NOT NULL,
PRIMARY KEY(essn,pno),
FOREIGN KEY (essn) REFERENCES project (employee),
FOREIGN KEY (pno) REFERENCES project (pnumber))""")

#### Exercise 39 - Using Constraints

 Rework your database by including different Constraints
 Use each of the six different constraints at least once
 Create a new table if needed to insert some FOREIGN
KEYs

#### Selections

Just as we saw in SQL you can create Selections in sqlite
 There are different approaches to see the results of the
selection
 Syntax for using a for loop:
 for row in cur.execute('SELECT * FROM decks'):
 print(row)

 Syntax for using fetchall()
 cur.execute('SELECT * FROM decks')
 rows = cur.fetchall()
 for row in rows:
 print(row)


#### Exercise 40 - Selections

 Try to create two selections for each of your tables
 Use the for loop variant for one selection and the fetchall()
method for the second one

#### Updating data

 Just like in SQL you can UPDATE your data inside the
tables with sqlite as well
 Syntax:
 sql_update_query = """Update SqliteDb_developers
set salary = 10000 where id = 4"""
 cursor.execute(sql_update_query)
 sqliteConnection.commit()

 There is also the method of using a function in combination
with placeholders (?)
 Syntax:
def updateSqliteTable(id, salary):
sql_update_query = """Update SqliteDb_developers
set salary = ? where id = ?"""
data = (salary, id)
cursor.execute(sql_update_query, data)
updateSqliteTable(3, 7500)

Last but not least there is a method of updating multiple
records by using the executemany method
 Syntax
def updateMultipleRecords(recordList):
sqlite_update_query = """Update
SqliteDb_developers set salary = ? where id = ?"""
cursor.executemany(sqlite_update_query,
recordList)
records_to_update = [(9700, 4), (7800, 5), (8400, 6)]

#### Exercise 42 – Updating data

 Update some of the data in your tables
 Use all of the three methods shown in the presentation at
least once





#########################################################################

import sqlite3

db = sqlite3.connect("DatabaseCQ.db")
cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS samplers")
cur.execute("DROP TABLE IF EXISTS keyboards")
cur.execute("DROP TABLE IF EXISTS speakers")
cur.execute("DROP TABLE IF EXISTS synths")
cur.execute("DROP TABLE IF EXISTS order_history")
cur.execute("DROP TABLE IF EXISTS vinyl")
cur.execute("DROP TABLE IF EXISTS accessories")

cur.execute(
    """CREATE TABLE samplers (id INTEGER primary key AUTOINCREMENT, Name TEXT NOT NULL, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE order_history (order_id integer NOT NULL PRIMARY KEY AUTOINCREMENT, Item_id FOREIGN KEY INTEGER (id) REFERENCES id (id), Date Ordered, Delivery Status, Orders)"""
)
db.commit()
db.close()

#### Selections

# Just as we saw in SQL you can create Selections in sqlite.
# There are different approaches to see the results of the selection

# Syntax for using a for loop:

# for

# Syntax:

# Syntax for using fetchall()

# cur.execute('SELECT * FROM decks')
# rows = cur.fetchall()
# for row in rows:
#         print(row)

#### Updating data

#Just like in SQL you can UPDATE your data inside the tables with sqlite as well

#Syntax:
    sql_update_query = """Update SqliteDb_developers
    set salary = 10000 where id = 4"""
    cursor.execute(sql_update_query)
    sqliteConnection.commit()

....
