#9.5 page 167

class User:
    """A simple model of a user."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
    
    def print_login_attempts(self):
        """Print login attempts."""
        print(f"{self.login_attempts}")

    def increment_login_attempts(self):
        """Increase login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0
    

    
user = User('Mark', 'Mywords', 19)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.print_login_attempts()

user.reset_login_attempts()
user.print_login_attempts()


