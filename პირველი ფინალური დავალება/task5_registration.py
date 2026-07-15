import string


class RegistrationSimulator:
    def __init__(self):
        self.database = {
            "email": "user@mail.com",
            "username": "george777",
            "password": "password123"
        }

    def register_name(self, name):
        if not name:
            return "შეცდომა: სახელი არ უნდა იყოს ცარიელი!"

        if any(char.isdigit() for char in name):
            return "შეცდომა: შემოყვანილია რიცხვი ან შერეული ციფრები. შეიყვანეთ მხოლოდ ასოები!"

        if any(not char.isalnum() for char in name):
            return "შეცდომა: შემოყვანილია სიმბოლოები. შეიყვანეთ მხოლოდ ასოები!"

        is_latin = all(char in string.ascii_letters for char in name)
        if not is_latin:
            return "ეს არის სხვა ენა. გთხოვთ გამოიყენოთ ლათინური ასოები"

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