import random
import logging

logging.basicConfig(
    filename="lottery.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)


class LotterySimulator:
    def __init__(self, jackpot_amount: float):
        self.jackpot = jackpot_amount

    def run_draw(self, player_numbers: list):
        winning_numbers = random.sample(range(1, 50), 6)
        matches = len(set(player_numbers) & set(winning_numbers))

        prize = 0.0
        if matches == 6:
            prize = self.jackpot
        elif matches == 5:
            prize = self.jackpot * 0.60
        elif matches == 4:
            prize = self.jackpot * 0.40
        elif matches == 3:
            prize = self.jackpot * 0.20

        log_msg = f"თამაში - მოთამაშე: {player_numbers} | მომგებიანი: {winning_numbers} | დამთხვევა: {matches} | მოგება: {prize} GEL"
        logging.info(log_msg)

        return winning_numbers, matches, prize


def main():
    simulator = LotterySimulator(100000.0)
    print("--- ლატარიის სიმულატორი (საპრიზო ფონდი: 100 000 GEL) ---")

    player_numbers = []
    for i in range(6):
        num = int(input(f"შეიყვანეთ {i + 1}-ე რიცხვი (1-დან 49-მდე): ").strip())
        player_numbers.append(num)

    winning, matches, prize = simulator.run_draw(player_numbers)

    print(f"\nმომგებიანი რიცხვებია: {winning}")
    print(f"თქვენი რიცხვები: {player_numbers}")
    print(f"დაგემთხვათ: {matches} რიცხვი")

    if prize > 0:
        if matches == 6:
            print(f"გილოცავთ! თქვენ მოიგეთ JACKPOT: {prize} GEL!")
        else:
            print(f"გილოცავთ! თქვენ მოიგეთ: {prize} GEL!")
    else:
        print("სამწუხაროდ ამჯერად ვერაფერი მოიგეთ.")


if __name__ == "__main__":
    main()