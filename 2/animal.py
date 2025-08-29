class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        print(f"{self.name} издает звук.")

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Вид: {self.species}")

    def __del__(self):
        print(f"Объект {self.name} удален.")
