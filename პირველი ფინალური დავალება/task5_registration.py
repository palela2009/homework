import string


class RegistrationSimulator:
    def __init__(self):
        self.database = {
            "email": "user@mail.com",
            "username": "george777",
            "password": "password123"
        }

    def register_name(self, name):
        if name.isdigit():
            return "შემოყვანილია რიცხვითი მნიშვნელობა, შემოიტანეთ მხოლოდ string პატარა რეგისტრში"

        is_ascii_letter = all(char in string.ascii_letters for char in name)

        if not is_ascii_letter:
            is_georgian = all('\u10a0' <= char <= '\u10ff' for char in name)
            if is_georgian or any(char.isalpha() for char in name):
                return "ეს არის სხვა ენა. გთხოვთ გამოიყენოთ ლათინური ასოები"
            else:
                return "შემოყვანილია სიმბოლოები, შემოიტანეთ მხოლოდ string პატარა რეგისტრში"

        if not name.islower():
            return "შემოიტანეთ მხოლოდ string პატარა რეგისტრში"

        self.database["name"] = name
        return self.database


def main():
    simulator = RegistrationSimulator()
    print("--- რეგისტრაციის სისტემა ---")
    name_input = input("შეიყვანეთ თქვენი სახელი (ლათინური პატარა ასოებით): ").strip()

    result = simulator.register_name(name_input)

    if isinstance(result, dict):
        print("\nრეგისტრაცია წარმატებით დასრულდა!")
        print(f"ელ-ფოსტა: {result['email']}")
        print(f"სახელი: {result['name']}")
        print(f"ზედმეტსახელი: {result['username']}")
        print(f"პაროლი: {result['password']}")
    else:
        print(result)


if __name__ == "__main__":
    main()