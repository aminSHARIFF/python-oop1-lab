#!/usr/bin/env python3

class Coffee:
    """
    Coffee class used to represent a coffee item in the bookstore.
    """

    def __init__(self, size, price):
        # Set size using property validation
        self.size = size

        # Store price directly
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Ensure size is one of the allowed options
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Increase price by 1 when tipping
        self.price += 1
        print("This coffee is great, here’s a tip!")
