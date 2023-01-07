ORDERS = [
{
    "id": 1,
    "metalId": 3,
    "sizeId": 2,
    "styleId": 3,
    "itemId": 1,
    "timestamp": 1614659931693
},
{
    "id": 2,
    "metalId": 1,
    "sizeId": 1,
    "styleId": 2,
    "itemId": 2,
    "timestamp": 1614659931694
}
]

def get_all_orders():
    """returns ORDERS list of dictionaries"""
    return ORDERS

def get_single_order(id):
    """Variable to hold the found order, if it exists"""
    requested_order = None
    for order in ORDERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if order["id"] == id:
            requested_order = order

    return requested_order


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
