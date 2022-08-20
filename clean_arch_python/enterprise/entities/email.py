import re


class Email:
    def __init__(self, value: str) -> None:
        if not re.match(r"[^@]+@[^@]+\.[^@]+", value):
            raise ValueError("Invalid email")
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value
