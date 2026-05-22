current_year = 2026

while True:
    age_input = input("გთხოვთ, შეიყვანოთ თქვენი ასაკი: ")

    try:
        age = int(age_input)
        if age < 0 or age > 120:
            print("შეიყვანეთ რეალური ასაკი")
            continue


        break

    except ValueError:

        print(" შეყვანილი მონაცემი არ არის რიცხვი")

birth_year = current_year - age
print(f"თქვენი დაბადების წელია : {birth_year}")