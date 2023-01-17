import sqlite3
import json
from models import Order


ORDERS = [
{
    "id": 1,
    "metalId": 3,
    "sizeId": 2,
    "styleId": 3,
    "timestamp": 1614659931693
},
{
    "id": 2,
    "metalId": 1,
    "sizeId": 1,
    "styleId": 2,
    "timestamp": 1614659931694
}
]

def get_all_orders():
   # Open a connection to the database
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM Orders o
        """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an order instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            order = Order(row['id'], row['metal_id'], row['size_id'],
                            row['style_id'], row['timestamp'])
                      
            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT *
        FROM Orders o
        WHERE o.id = ?
        """, (id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        order = Order(data['id'], data['metal_id'], data['size_id'],
                      data['style_id'], data['timestamp'])

        return order.__dict__


def create_order(order):
    """Creates a new order dictionary in the ORDERS list of dictionaries"""
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the order dictionary
    order["id"] = new_id

    # Add the order dictionary to the list {append is similar to push}
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    """remove order dictionary from the list"""
    # Initial -1 value for order index, in case one isn't found
    order_index = -1

    # Iterate the ORDER list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Store the current index.
            order_index = index

    # If the order was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
        # Iterate the ORDERS list, but use enumerate() so that
        # you can access the index value of each item.
    """iterates the list of orders until it finds the right one, and then replaces it with what the client sent as the replacement."""
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the order. Update the value.
            ORDERS[index] = new_order
            break           
