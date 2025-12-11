class Person:
    """Человек с именем и возрастом."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = int(age)

    def introduce(self) -> None:
        print(f"Меня зовут {self.name}, мне {self.age} лет")
