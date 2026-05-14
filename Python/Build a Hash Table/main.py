class HashTable:
    def __init__(self):
        # Must use self. to make it an instance attribute
        # Initialized to an empty dictionary per user stories
        self.collection = {}

    def hash(self, value):
        # Sum of Unicode values
        sum_chars = 0
        for char in value:
            sum_chars += ord(char)
        return sum_chars

    def add(self, key, value):
        # Call the instance method using self.hash
        h = self.hash(key)
        # Handle collisions with a nested dictionary
        if h not in self.collection:
            self.collection[h] = {}
        self.collection[h][key] = value

    def remove(self, key):
        h = self.hash(key)
        # Check if key exists before deleting to avoid errors
        if h in self.collection and key in self.collection[h]:
            del self.collection[h][key]

    def lookup(self, key):
        h = self.hash(key)
        # Return the value if found, otherwise return None
        if h in self.collection:
            return self.collection[h].get(key)
        return None