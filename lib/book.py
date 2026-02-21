#!/usr/bin/env python3

class Book:
    """
    Book class used to represent a book in the bookstore.
    """

    def __init__(self, title, page_count):
        # Store the title provided by the user
        self.title = title

        # Use the property setter to validate page_count
        self.page_count = page_count

    @property
    def page_count(self):
        # Return the stored page count
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Make sure page_count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Simulate flipping a page
        print("Flipping the page...wow, you read fast!")
