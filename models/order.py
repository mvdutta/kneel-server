class Order():
    """Class that defines the properties for a order object"""
    # Write the __init__ method here

    def __init__(self, id, metal_id, size_id, style_id, item_id, timestamp):
        self.id = id
        self.metal_id = metal_id
        self.size_id = size_id
        self.style_id = style_id
        self.item_id = item_id
        self.timestamp = timestamp
