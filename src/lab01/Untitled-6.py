class Vehicle:
    def __init__(self, brand: str, speed: int):
        self._brand = brand
        self._speed = speed

    def describe(self):
        return f"{self._brand}, макс. скорость: {self._speed} км/ч"

class Car(Vehicle):
    def __init__(self, brand: str, speed: int, doors: int):
        super().__init__(brand, speed)
        self._doors = doors

    def describe(self):
        base = super().describe()
        return f"{base}, дверей: {self._doors}"

c = Car("Toyota", 180, 4)
print(c.describe())