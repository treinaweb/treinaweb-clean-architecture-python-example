import pytest

from clean_arch_python.enterprise.entities.email import Email


def test_create_email_without_at_symbol_should_raise_value_error():
    expected_message = "Invalid email"
    with pytest.raises(ValueError) as e:
        Email("testmail.com")
    assert expected_message == str(e.value)


def test_create_email_without_dot_symbol_should_raise_value_error():
    expected_message = "Invalid email"
    with pytest.raises(ValueError) as e:
        Email("test@mailcom")
    assert expected_message == str(e.value)


def test_create_email_with_invalid_domain_should_raise_value_error():
    expected_message = "Invalid email"
    with pytest.raises(ValueError) as e:
        Email("test@mailcom.")
    assert expected_message == str(e.value)


def test_create_email_with_valid_email_should_not_raise_value_error():
    email = Email("test@mail.com")
    assert email.value == "test@mail.com"
