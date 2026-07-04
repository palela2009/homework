import pytest

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
    assert celsius_to_fahrenheit(25) == pytest.approx(77.0)
    assert celsius_to_fahrenheit(-40) == pytest.approx(-40.0)
    assert celsius_to_fahrenheit(36.6) == pytest.approx(97.88)


USERS_DB = {"admin": "password123", "user1": "securepass"}

def login_user(username, password):
    if username not in USERS_DB or USERS_DB[username] != password:
        raise ValueError("Invalid username or password")
    return True

def test_login_success():
    assert login_user("admin", "password123") is True

def test_login_fail():
    with pytest.raises(ValueError):
        login_user("admin", "wrong_password")
    with pytest.raises(ValueError):
        login_user("unknown_user", "password123")


def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email

@pytest.mark.parametrize("email, expected", [
    ("test@example.com", True),
    ("user.name@domain.ge", True),
    ("invalidemail.com", False),
    ("test@domain", False),
    ("plain_text", False)
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected