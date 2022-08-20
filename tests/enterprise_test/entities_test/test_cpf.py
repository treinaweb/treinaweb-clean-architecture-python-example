import pytest

from clean_arch_python.enterprise.entities.cpf import Cpf


def test_create_cpf_with_letters_should_raise_exception():
    expected_message = "Cpf must have digits only"
    with pytest.raises(ValueError) as e:
        Cpf("1234567890a")
    assert expected_message == str(e.value)


def test_create_cpf_with_less_than_11_digits_should_raise_exception():
    expected_message = "Cpf must have 11 digits"
    with pytest.raises(ValueError) as e:
        Cpf("123456789")
    assert expected_message == str(e.value)


def test_create_cpf_with_more_than_11_digits_should_raise_exception():
    expected_message = "Cpf must have 11 digits"
    with pytest.raises(ValueError) as e:
        Cpf("123456789011")
    assert expected_message == str(e.value)


def test_create_cpf_with_special_characters_should_raise_exception():
    expected_message = "Cpf must have digits only"
    with pytest.raises(ValueError) as e:
        Cpf("123456789@1")
    assert expected_message == str(e.value)


def test_create_cpf_with_digits_only_should_not_raise_exception():
    cpf = Cpf("12345678901")
    assert cpf.value == "12345678901"
