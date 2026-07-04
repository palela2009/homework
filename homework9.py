import random


class Character:
    def __init__(self, name: str, health: int, power: int):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, other):
        if isinstance(self, Warrior) and isinstance(other, Mage):
            other.health = 0
            print(f"{self.name} (Warrior) defeated {other.name} (Mage)!")
        elif isinstance(self, Mage) and isinstance(other, Archer):
            other.health = 0
            print(f"{self.name} (Mage) defeated {other.name} (Archer)!")
        elif isinstance(self, Archer) and isinstance(other, Warrior):
            other.health = 0
            print(f"{self.name} (Archer) defeated {other.name} (Warrior)!")
        else:
            other.health -= self.power
            if other.health <= 0:
                print(f"{self.name} defeated {other.name}!")
            else:
                print(f"{self.name} attacked {other.name}. Remaining health: {other.health}")


class Warrior(Character):
    def __init__(self, name: str, health: int, power: int):
        super().__init__(name, health, power)


class Mage(Character):
    def __init__(self, name: str, health: int, power: int):
        super().__init__(name, health, power)


class Archer(Character):
    def __init__(self, name: str, health: int, power: int):
        super().__init__(name, health, power)


print("--- ამოცანა 1 ---")
w = Warrior("Gimli", 100, 20)
m = Mage("Gandalf", 80, 25)
a = Archer("Legolas", 90, 22)

w.attack(m)

m = Mage("Gandalf", 80, 25)
m.attack(a)

a = Archer("Legolas", 90, 22)
a.attack(w)


class Monster:
    def __init__(self, name: str, level: int, ability: str):
        self.name = name
        self.level = level
        self.ability = ability

    @classmethod
    def create_from_level(cls, level: int):
        names_pool = {
            1: ["Sparky", "Bubbles"],
            2: ["Cloudy", "Sunny"],
            3: ["Friendly", "Buddy"],
            4: ["Happy", "Joy"],
            5: ["Helper", "Healer"]
        }
        abilities = {1: "Lights rooms", 2: "Makes rain", 3: "Carries bags", 4: "Cheers people", 5: "Cures colds"}

        current_level = level if level in names_pool else 1
        name = random.choice(names_pool[current_level])
        ability = abilities[current_level]
        return cls(name, level, ability)


print("\n--- ამოცანა 2 ---")
monsters = [Monster.create_from_level(random.randint(1, 5)) for _ in range(10)]
for monster in monsters:
    print(f"Monster: {monster.name}, Level: {monster.level}, Help: {monster.ability}")


class SlotMachine:
    def __init__(self, pool: list):
        self.pool = pool

    @staticmethod
    def generate_symbols(pool: list) -> list:
        return [random.choice(pool) for _ in range(3)]

    @classmethod
    def from_difficulty(cls, level: str):
        if level == "easy":
            return cls(["A", "B"])
        elif level == "medium":
            return cls(["A", "B", "C"])
        else:
            return cls(["A", "B", "C", "D", "E"])

    def play(self):
        result = self.generate_symbols(self.pool)
        print(f"Slots: {result}")
        if result[0] == result[1] == result[2]:
            print("You won!")
        else:
            print("You lost!")


print("\n--- ამოცანა 3 ---")
machine_easy = SlotMachine.from_difficulty("easy")
machine_easy.play()
machine_hard = SlotMachine.from_difficulty("hard")
machine_hard.play()


class Hero:
    def __init__(self, name: str, health: int = 100, score: int = 0):
        self.name = name
        self.__health = health
        self.__score = score

    @staticmethod
    def random_event() -> dict:
        events = [
            {"type": "score", "value": 20},
            {"type": "damage", "value": 30}
        ]
        return random.choice(events)

    @classmethod
    def from_name(cls, name: str):
        return cls(name)

    def get_health(self):
        return self.__health

    def get_score(self):
        return self.__score

    def change_health(self, value: int):
        self.__health += value

    def change_score(self, value: int):
        self.__score += value


class SuperHero(Hero):
    def __init__(self, name: str, power: str):
        super().__init__(name)
        self.power = power


print("\n--- ამოცანა 4 ---")
hero = SuperHero.from_name("Peter")
print(f"Hero {hero.name} started the game.")

while hero.get_health() > 0:
    event = hero.random_event()
    if event["type"] == "score":
        hero.change_score(event["value"])
        print(f"Found treasure! Score: {hero.get_score()}")
    elif event["type"] == "damage":
        hero.change_health(-event["value"])
        print(f"Took damage! Remaining Health: {hero.get_health()}")

print("Game Over!")


class Card:
    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self, cards: list):
        self.__cards = cards

    @classmethod
    def create_standard_deck(cls):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        cards = [Card(rank, suit) for suit in suits for rank in ranks]
        return cls(cards)

    @staticmethod
    def shuffle(cards: list):
        random.shuffle(cards)

    def get_cards(self):
        return self.__cards

    def draw_five(self) -> list:
        hand = self.__cards[:5]
        self.__cards = self.__cards[5:]
        return hand


print("\n--- ამოცანა 5 ---")
deck = Deck.create_standard_deck()
cards_list = deck.get_cards()
Deck.shuffle(cards_list)

hand = deck.draw_five()
print(f"Player's hand: {hand}")

ranks_in_hand = [card.rank for card in hand]
has_pair = False
for rank in ranks_in_hand:
    if ranks_in_hand.count(rank) >= 2:
        has_pair = True
        break

if has_pair:
    print("Simple combination found: You have a pair!")
else:
    print("No combination found.")