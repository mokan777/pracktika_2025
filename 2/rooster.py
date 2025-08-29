from animal import Animal

class Rooster(Animal):
    def __init__(self, name, age, species, color, crow_level):
        super().__init__(name, age, species)
        self.color = color          # цвет петуха
        self.crow_level = crow_level  # громкость крика (например, от 1 до 10)

    def info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Вид: {self.species}, "
              f"Цвет: {self.color}, Уровень крика: {self.crow_level}")

    def crow(self):
        print(f"{self.name} кричит 'Ку-ка-ре-ку!' с громкостью {self.crow_level}!")
