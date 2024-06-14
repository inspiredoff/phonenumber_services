from dataclasses import dataclass


@dataclass
class Person:
    last_name: str
    first_name: str
    number_telephone: str
    info: str

    def __repr__(self):
        return f"{self.last_name}, {self.first_name}, {self.number_telephone}, {self.info}"
