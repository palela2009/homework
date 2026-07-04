import sys
from dataclasses import dataclass

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            print(f"დეპოზიტი: +{amount}. მიმდინარე ბალანსი: {self.__balance}")
        else:
            print("თანხა უნდა იყოს დადებითი!")

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"გატანა: -{amount}. მიმდინარე ბალანსი: {self.__balance}")
        else:
            print("არასაკმარისი თანხა ან არასწორი ოდენობა!")

    def get_balance(self):
        return self.__balance


print("--- ამოცანა 1 ---")
acc = BankAccount("გიორგი", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)
print("ბალანსი მეთოდით:", acc.get_balance())


class ShoppingCart:
    def __init__(self, items: list):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __eq__(self, other):
        if isinstance(other, ShoppingCart):
            return len(self) == len(other)
        return False


print("\n--- ამოცანა 2 ---")
cart1 = ShoppingCart(["apple", "banana"])
cart2 = ShoppingCart(["milk", "bread"])
cart3 = ShoppingCart(["juice"])
cart4 = ShoppingCart(["water", "cheese"])

print("2 კალათის შედარება (cart1 == cart2):", cart1 == cart2)
print("3 კალათის შედარება (cart1 == cart2 == cart3):", cart1 == cart2 == cart3)
print("4 კალათის შედარება (cart1 == cart2 == cart4):", cart1 == cart2 == cart4)


@dataclass
class Book:
    title: str
    author: str
    year: int

    def is_classic(self) -> bool:
        return self.year < 1970


print("\n--- ამოცანა 3 ---")
book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი", 1200)
book2 = Book("Harry Potter", "J.K. Rowling", 1997)

print(f"'{book1.title}' არის კლასიკა?:", book1.is_classic())
print(f"'{book2.title}' არის კლასიკა?:", book2.is_classic())


class Person:
    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print("Person removed")


print("\n--- ამოცანა 4 ---")
p1 = Person("ნიკა")
del p1


class Temperature:
    def __init__(self, celsius: float):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value: float):
        self.__celsius = value

    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32


print("\n--- ამოცანა 5 ---")
temp = Temperature(25)
print(f"25°C ფარენგეიტში არის: {temp.fahrenheit}°F")
temp.celsius = 0
print(f"ცელსიუსის 0-ზე შეცვლის შემდეგ, ფარენგეიტია: {temp.fahrenheit}°F")


class CustomList:
    def __init__(self, *args):
        self.data = list(args)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __iter__(self):
        return iter(self.data)


print("\n--- ამოცანა 6 ---")
my_list = CustomList(10, 20, 30)
my_list[1] = 99

print("ელემენტები ციკლში:")
for item in my_list:
    print(item)


class Refrigerator:
    def __init__(self):
        self.items = []

    def add_item(self, item: str):
        self.items.append(item)

    def __contains__(self, item):
        return item in self.items

    def __str__(self):
        return f"Fridge with {len(self.items)} items"

    def __del__(self):
        print("Fridge unplugged!")


print("\n--- ამოცანა 7 ---")
fridge = Refrigerator()
fridge.add_item("milk")
fridge.add_item("cheese")

print("არის რძე მაცივარში?:", "milk" in fridge)
print(fridge)
del fridge


class FunnyCalculator:
    def __add__(self, other):
        return "Why are you adding numbers? Just buy a calculator"

    def __mul__(self, other):
        return "Multiplication is too mainstream..."

    def __truediv__(self, other):
        if other == 0:
            print("ZeroDivisionError? Nah, let’s just say infinity")
            return None
        return "Dividing with fun!"

    def __rtruediv__(self, other):
        print("ZeroDivisionError? Nah, let’s just say infinity")
        return None

    def __str__(self):
        return "I’m the funniest calculator in Python!"


print("\n--- ამოცანა 8 ---")
calc = FunnyCalculator()

print("calc + 5:", calc + 5)
print("calc * 2:", calc * 2)
print("10 / calc:")
10 / calc
print("სტრუქტურა:", calc)