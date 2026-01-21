"""
Demonstrates flexible function interfaces in Python.

Focus:
- *args for variable positional arguments
- **kwargs for flexible keyword-based metadata
"""

def log_actions(*actions):
    """Log an arbitrary number of actions."""
    for action in actions:
        print(f"Action: {action}")


def build_profile(first_name, last_name, **metadata):
    """Build a flexible user profile."""
    profile = {
        "first_name": first_name,
        "last_name": last_name,
    }
    profile.update(metadata)
    return profile


if __name__ == "__main__":
    log_actions("login", "view_dashboard", "logout")

    user = build_profile(
        "Alla",
        "Vardi",
        location="Paris",
        field="Cybersecurity",
        focus="Learning Python"
    )

    print(user)
