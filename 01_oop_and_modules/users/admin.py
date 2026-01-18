from user import User

class Privileges:
    """A class to store and show admin privileges."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        """Print a statement describing priveleges"""
        print(f"This user has these privileges:")
        for privilege in self.privileges:
            print(f"- {privilege.title()}")

class Admin(User):
    """Creating Admin"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize attributes of the parent calass.
        Then initialize attributes specific to the admin.
        """
        super().__init__(first_name, last_name, age)
        
        self.privileges = Privileges()
