import logging

logging.basicConfig(
    filename="atm_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    encoding="utf-8"
)


class ATM:
    def __init__(self, initial_balance: float):
        self.balance = initial_balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount: float) -> bool:
        if amount > 1000:
            return False
        self.balance += amount
        logging.info(f"შემოტანა: +{amount} GEL | ბალანსი: {self.balance} GEL")
        return True

    def withdraw(self, amount: float) -> bool:
        if amount > self.balance:
            return False
        self.balance -= amount
        logging.info(f"გატანა: -{amount} GEL | ბალანსი: {self.balance} GEL")
        return True


def main():
    atm = ATM(500.0)
    while True:
        print("\n--- ბანკომატი (GEL) ---")
        print("1. ბალანსის შემოწმება")
        print("2. თანხის შემოტანა")
        print("3. თანხის გატანა")
        print("4. გასვლა")

        choice = input("აირჩიეთ ოპერაცია (1-4): ").strip()

        if choice == "1":
            print(f"თქვენი მიმდინარე ბალანსია: {atm.check_balance()} ლარი")
        elif choice == "2":
            amount = float(input("შეიყვანეთ შესატანი თანხა: ").strip())
            if atm.deposit(amount):
                print("თანხა წარმატებით შემოტანილია!")
            else:
                print("შეცდომა: ერთჯერადად 1000 ლარზე მეტის შემოტანა აკრძალულია!")
        elif choice == "3":
            amount = float(input("შეიყვანეთ გასატანი თანხა: ").strip())
            if atm.withdraw(amount):
                print("თანხა წარმატებით გატანილია!")
            else:
                print("შეცდომა: ანგარიშზე არ არის საკმარისი თანხა!")
        elif choice == "4":
            break


if __name__ == "__main__":
    main()