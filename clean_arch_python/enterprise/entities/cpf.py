class Cpf:
    def __init__(self, value: str) -> None:
        if len(value) != 11:
            raise ValueError("Cpf must have 11 digits")
        if not value.isdigit():
            raise ValueError("Cpf must have digits only")
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value
