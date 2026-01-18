class User:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Print a description of the user."""
        print(f"{self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
