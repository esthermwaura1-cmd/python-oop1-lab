#!/usr/bin/env python3

class Coffee:
    pass#!/usr/bin/env python3

class Coffee:
    def init(self, size, price):
        """Initialize a Coffee with size and price."""
        self._size = None
        self.size = size  # Use property setter for validation
        self.price = price

    @property
    def size(self):
        """Get the size of the coffee."""
        return self._size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        valid_sizes = ["Small", "Medium", "Large"]
        if value in valid_sizes:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")
            self._size = None

    def tip(self):
        """Add a tip to the coffee."""
        print("This coffee is great, here’s a tip!")
        self.price += 1