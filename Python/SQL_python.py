#### Python SQL libraries

...

# Main job of these libraries is to give you access to a way to communicate with your database.

...


#### SQLite

import sqlite3


#### Connect to your database

# def updateTable(Name, Price, Wins):
#     sql_update_query = """Update decks SET Price = ?, Wins = ? where Short = ?"""
#     data = (Price, Wins, Name)
#     cur.execute(sql_update_query,data)
#
# db = sqlite3.connect('DatabaseCQ.db')
#
# #### The Cursor object
#
# cur = db.cursor()


#### Creating tables

# To create tables...

# cur.execute('''CREATE TABLE decks (Short varchar(255), Colors varchar(255), FullName varchar(255), Price real, Wins int)''')
# cur.execute("INSERT INTO decks VALUES ('Arix','UG','Arixmethes, the Slumbering Isle',450.28,5)")
# for row in cur.execute('SELECT * FROM decks'):
#     print(row)

# real data type for float variables


#### Closing your database

# con.close()

#### Your database

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

cur.execute(
    """CREATE TABLE keyboards (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)
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

cur.execute(
    """CREATE TABLE speakers (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE synths (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)
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


cur.execute(
    """CREATE TABLE order_history (order_id integer NOT NULL primary key autoincrement, Item, Item_id, Date Ordered, Delivery Status, Orders)"""
)

cur.execute(
    """CREATE TABLE vinyl (id integer primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

cur.execute(
    """CREATE TABLE accessories (id integer NOT NULL primary key autoincrement, Name, Manufacturer, Price, Quantity_In_Stock)"""
)

db.commit()
db.close()

####

### Constraints

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
