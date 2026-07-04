import random
from abc import ABC, abstractmethod


class MazeGame:
    def __init__(self):
        self.maze = [
            ["S", ".", "#", ".", "."],
            ["#", ".", "#", ".", "#"],
            [".", ".", ".", ".", "."],
            ["#", "#", "#", ".", "#"],
            [".", ".", ".", ".", "E"]
        ]
        self.reset_position()

    def reset_position(self):
        self.row = 0
        self.col = 0

    def play(self):
        while True:
            direction = input("საით გსურთ წასვლა? (მაღლა, დაბლა, მარცხნივ, მარჯვნივ): ").strip()
            new_row, new_col = self.row, self.col

            if direction == "მაღლა":
                new_row -= 1
            elif direction == "დაბლა":
                new_row += 1
            elif direction == "მარცხნივ":
                new_col -= 1
            elif direction == "მარჯვნივ":
                new_col += 1

            if 0 <= new_row < len(self.maze) and 0 <= new_col < len(self.maze[0]):
                cell = self.maze[new_row][new_col]
                if cell == "#":
                    print("თქვენ შეეჯახეთ კედელს! თამაში იწყება თავიდან.")
                    self.reset_position()
                elif cell == "." or cell == "S":
                    print("სწორი გზაა, განაგრძეთ!")
                    self.row, self.col = new_row, new_col
                elif cell == "E":
                    print("შენ გაიარე ლაბირინთი")
                    break
            else:
                print("ლაბირინთს გარეთ ვერ გახვალთ! თამაში იწყება თავიდან.")
                self.reset_position()


print("--- ამოცანა 1 ---")


# maze_game = MazeGame()
# maze_game.play()


class Fighter:
    def __init__(self, name: str, health: int, skills: dict):
        self.name = name
        self.health = health
        self.skills = skills


def get_fighters_pool():
    return {
        "გიგანტი": Fighter("გიგანტი", 150, {"მიწისძვრა": 20, "ქვის სროლა": 15, "ძლიერი დარტყმა": 25}),
        "სწრაფი": Fighter("სწრაფი", 90, {"ელვა": 25, "ქარის დანა": 20, "სწრაფი თავდასხმა": 15}),
        "მოქნილი": Fighter("მოქნილი", 100, {"აკრობატიკა": 18, "ჩრდილის დარტყმა": 22, "ორმაგი გასროლა": 20}),
        "აქილევსი": Fighter("აქილევსი", 120, {"ხმლის ჩეხვა": 22, "ფარის დარტყმა": 15, "გმირული შეტევა": 28}),
        "პითონისტი": Fighter("პითონისტი", 110, {"SyntaxError სროლა": 30, "უსასრულო ციკლი": 25, "ბაგის გაშვება": 20})
    }


def play_1vs1():
    pool = get_fighters_pool()
    print("ხელმისაწვდომი მებრძოლები:", list(pool.keys()))

    p1_choice = input("მოთამაშე 1, აირჩიე გმირი: ").strip()
    p2_choice = input("მოთამაშე 2, აირჩიე გმირი: ").strip()

    p1 = get_fighters_pool()[p1_choice]
    p2 = get_fighters_pool()[p2_choice]

    p1.name = "მოთამაშე 1 (" + p1.name + ")"
    p2.name = "მოთამაშე 2 (" + p2.name + ")"

    current_turn = p1
    opponent = p2

    while p1.health > 0 and p2.health > 0:
        print(f"\nრიგია: {current_turn.name}")
        print("ხელმისაწვდომი სკილები:", list(current_turn.skills.keys()))
        chosen_skill = input("აირჩიე სკილი: ").strip()

        damage = current_turn.skills[chosen_skill]
        opponent.health -= damage
        print(f"{current_turn.name}-მა გამოიყენა {chosen_skill} და მიაყენა {damage} ზიანი!")
        print(f"{opponent.name}-ის დარჩენილი სიცოცხლე: {max(0, opponent.health)}")

        current_turn, opponent = opponent, current_turn

    winner = p1 if p1.health > 0 else p2
    print(f"\nთამაში დასრულდა! გაიმარჯვა {winner.name}-მა!")


print("\n--- ამოცანა 2 ---")


# play_1vs1()


class PlanetaryBody(ABC):
    @abstractmethod
    def rotate(self):
        pass


class Earth(PlanetaryBody):
    def __init__(self, population: int, oxygen_level: int):
        self._population = population
        self.__oxygen_level = oxygen_level

    def rotate(self):
        return "Earth rotates around its axis in 24 hours."

    def get_oxygen(self):
        return self.__oxygen_level

    def set_oxygen(self, value):
        if 0 <= value <= 100:
            self.__oxygen_level = value


class HumanActivity:
    def live(self):
        return "Humans are building cities."


class Continent(Earth):
    def __init__(self, name: str, population: int, oxygen_level: int):
        super().__init__(population, oxygen_level)
        self.name = name

    def rotate(self):
        return f"Continent {self.name} moves slightly due to tectonic plates while Earth rotates."


class Ocean(Earth):
    def __init__(self, name: str, population: int, oxygen_level: int):
        super().__init__(population, oxygen_level)
        self.name = name

    def rotate(self):
        return f"Ocean currents flow on {self.name} as Earth rotates."


class CivilizedZone(Earth, HumanActivity):
    def __init__(self, city_count: int, population: int, oxygen_level: int):
        super().__init__(population, oxygen_level)
        self.city_count = city_count


print("\n--- ამოცანა 3 ---")
cont = Continent("Eurasia", 5000000000, 21)
ocean = Ocean("Pacific", 0, 21)
zone = CivilizedZone(500, 1000000, 20)

print(cont.rotate())
print(ocean.rotate())
print(zone.live())
print(f"Earth Oxygen Level via encapsulation: {cont.get_oxygen()}%")


class WitchPot:
    def __init__(self):
        self.ingredients = ["ღამურა", "ბუმბული", "ვაშლი", "ყვავილი", "წყალი"]
        self.recipes = {
            frozenset(["ვაშლი", "წყალი"]): "ვაშლის წვენი",
            frozenset(["ღამურა", "წყალი"]): "უხილავობის ელექსირი",
            frozenset(["ბუმბული", "ყვავილი"]): "ფრენის ფხვნილი",
            frozenset(["ღამურა", "ბუმბული"]): "ღამის მაცნე",
            frozenset(["ვაშლი", "ყვავილი"]): "სურნელოვანი ჯემი",
            frozenset(["ბუმბული", "წყალი"]): "მჩატე სითხე",
            frozenset(["ღამურა", "ყვავილი"]): "შხამიანი ნექტარი",
            frozenset(["ვაშლი", "ბუმბული"]): "ჯადოსნური ხილი",
            frozenset(["ყვავილი", "წყალი"]): "ვარდის წყალი",
            frozenset(["ღამურა", "ვაშლი"]): "აკრძალული ნაყოფი"
        }

    def brew(self):
        print("ხელმისაწვდომი ინგრედიენტები:", self.ingredients)
        ing1 = input("აირჩიეთ პირველი ინგრედიენტი: ").strip()
        ing2 = input("აირჩიეთ მეორე ინგრედიენტი: ").strip()

        combination = frozenset([ing1, ing2])
        if combination in self.recipes:
            print(f"შედეგი: {ing1} + {ing2} = {self.recipes[combination]}")
        else:
            print("ასეთი კომბინაცია შეუძლებელია!")


print("\n--- ამოცანა 4 ---")


# pot = WitchPot()
# pot.brew()


class Transport(ABC):
    def __init__(self, fuel: float, speed: float, capacity: int):
        self.__fuel = fuel
        self.speed = speed
        self.capacity = capacity

    def get_fuel(self):
        return self.__fuel

    def set_fuel(self, amount):
        self.__fuel = amount

    @abstractmethod
    def move(self, distance: float):
        pass


class Car(Transport):
    def move(self, distance: float):
        needed_fuel = distance * 0.1
        if self.get_fuel() >= needed_fuel:
            self.set_fuel(self.get_fuel() - needed_fuel)
            print(f"Car moved {distance} km. Remaining fuel: {self.get_fuel()}")
        else:
            print("Car does not have enough fuel!")


class Bus(Transport):
    def move(self, distance: float):
        needed_fuel = distance * 0.3
        if self.get_fuel() >= needed_fuel:
            self.set_fuel(self.get_fuel() - needed_fuel)
            print(f"Bus moved {distance} km. Remaining fuel: {self.get_fuel()}")
        else:
            print("Bus does not have enough fuel!")


class Bike(Transport):
    def move(self, distance: float):
        print(f"Bike moved {distance} km. No fuel needed! Remaining fuel: {self.get_fuel()}")


print("\n--- ამოცანა 5 ---")
car = Car(50, 120, 5)
bus = Bus(100, 80, 40)
bike = Bike(0, 25, 1)

car.move(100)
bus.move(100)
bike.move(20)