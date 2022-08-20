import pytest

from clean_arch_python.enterprise.entities.client import ClientName, Client


def test_create_client_name_with_digits_should_raise_value_error():
    expected_message = "Client name must have letters only"
    with pytest.raises(ValueError) as e:
        ClientName("123")
    assert expected_message == str(e.value)


def test_create_client_name_with_less_than_3_letters_should_raise_value_error():
    expected_message = "Client name must have at least 3 letters"
    with pytest.raises(ValueError) as e:
        ClientName("te")
    assert expected_message == str(e.value)


def test_create_client_name_with_letters_only_should_not_raise_value_error():
    client_name = ClientName("test")
    assert client_name.value == "test"


def test_create_client_with_invalid_first_name_should_raise_value_error():
    with pytest.raises(ValueError):
        Client("", "test", "test@mail.com", "12345678912")


def test_create_client_with_invalid_last_name_should_raise_value_error():
    with pytest.raises(ValueError):
        Client("test", "", "test@mail.com", "12345678912")


def test_create_client_with_invalid_email_should_raise_value_error():
    with pytest.raises(ValueError):
        Client("test", "test", "test", "12345678912")


def test_create_client_with_invalid_cpf_should_raise_value_error():
    with pytest.raises(ValueError):
        Client("test", "test", "test@mail.com", "123456789")


def test_create_client_with_valid_data_should_not_raise_value_error():
    client = Client("test", "test", "test@mail.com", "12345678912")
    assert client.first_name == "test"
    assert client.last_name == "test"
    assert client.email == "test@mail.com"
    assert client.cpf == "12345678912"
