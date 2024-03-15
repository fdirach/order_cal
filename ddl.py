from conn import *
from data import *

# Drop
drop('Item')
drop('Vat')
drop('Offer')
drop('Customer')
drop('Purchase')

# Create tables
create_Item_table = """
CREATE TABLE IF NOT EXISTS Item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL
);
"""
execute_query(connection, create_Item_table)

create_Vat_table = """
CREATE TABLE IF NOT EXISTS Vat (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    vat INT
);
"""
execute_query(connection, create_Vat_table)

create_Offer_table = """
CREATE TABLE IF NOT EXISTS Offer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    offer_limits INT,
    offer_rate INT
);
"""
execute_query(connection, create_Offer_table)

create_Customer_table = """
CREATE TABLE IF NOT EXISTS Customer (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    mail TEXT,
    address TEXT
);
"""
execute_query(connection, create_Customer_table)

create_Purchase_table = """
CREATE TABLE IF NOT EXISTS Purchase (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    num_items INT,
    total_price REAL,
    customer_id,
    item_id,
    vat_id,
    offer_id,
    FOREIGN KEY (customer_id) REFERENCES customer(id),
    FOREIGN KEY (item_id) REFERENCES item(id),
    FOREIGN KEY (vat_id) REFERENCES vat(id),
    FOREIGN KEY (offer_id) REFERENCES offer(id)
);
"""
execute_query(connection, create_Purchase_table)


# Insert data from lists
insert_query_item = "INSERT INTO Item (name, price) VALUES (?, ?)"
for entry in item_list:
    execute_query_with_data(connection, insert_query_item, entry)

insert_query_vat = "INSERT INTO Vat (country, vat) VALUES (?, ?)"
for entry in vat_list:
    execute_query_with_data(connection, insert_query_vat, entry)

insert_query_offer = "INSERT INTO Offer (offer_limits, offer_rate) VALUES (?, ?)"
for entry in offer_list:
    execute_query_with_data(connection, insert_query_offer, entry)

# Insert data from userinputs
    



