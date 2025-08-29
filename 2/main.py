from rooster import Rooster

# Создаем объект класса Rooster
rooster1 = Rooster(name="Петя", age=2, species="Петух", color="Красный", crow_level=9)

rooster1.info()
rooster1.make_sound()  # Метод из родительского класса
rooster1.crow()        # Метод петуха

# Удаляем объект
del rooster1
