import random


class Blackjack:
    def __init__(self):
        suits = ["ყვავი", "ჯვარი", "გული", "აგური"]
        ranks = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
            "Jack": 10, "Queen": 10, "King": 10, "Ace": 11
        }
        self.deck = [{"card": f"{rank} {suit}", "value": val} for suit in suits for rank, val in ranks.items()]
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop()

    def calculate_score(self, hand):
        return sum(card["value"] for card in hand)

    def play(self):
        player_hand = [self.draw_card(), self.draw_card()]
        computer_hand = [self.draw_card(), self.draw_card()]

        while True:
            player_score = self.calculate_score(player_hand)
            print(f"\nთქვენი კარტები: {[c['card'] for c in player_hand]} (ქულა: {player_score})")

            if player_score >= 21:
                break

            choice = input("გსურთ დამატება? (add / stop): ").strip().lower()
            if choice == "add":
                player_hand.append(self.draw_card())
            elif choice == "stop":
                break

        player_score = self.calculate_score(player_hand)
        if player_score > 21:
            print(f"თქვენი ქულაა: {player_score}. თქვენ წააგეთ")
            return

        while self.calculate_score(computer_hand) < 17:
            computer_hand.append(self.draw_card())

        computer_score = self.calculate_score(computer_hand)
        print(f"\nკომპიუტერის კარტები: {[c['card'] for c in computer_hand]} (ქულა: {computer_score})")

        if computer_score > 21:
            print("კომპიუტერმა გადააჭარბა. თქვენ მოიგეთ")
        elif player_score > computer_score:
            print("თქვენ მოიგეთ")
        elif player_score < computer_score:
            print("თქვენ წააგეთ")
        else:
            print("ფრეა! ვიწყებთ თავიდან...")
            game = Blackjack()
            game.play()


if __name__ == "__main__":
    game = Blackjack()
    game.play()