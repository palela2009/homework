print("დავალება 1")
import random

def contains_georgian(text):
    georgian_alphabet = "აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭხჯჰ"
    for char in text:
        if char in georgian_alphabet:
            return True
    return False

while True:
    length_input = input("შეიყვანეთ პაროლის სიგრძე: ")
    if contains_georgian(length_input):
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        continue
    if length_input.isdigit():
        length = int(length_input)
        break
    else:
        print("გთხოვთ შეიყვანოთ ვალიდური რიცხვი.")

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>/?"

character_pool = ""

while True:
    ans = input("გსურთ პატარა ასოები? (y/n): ")
    if contains_georgian(ans):
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        continue
    if ans.lower() == 'y':
        character_pool += lower_letters
        break
    elif ans.lower() == 'n':
        break

while True:
    ans = input("გსურთ დიდი ასოები? (y/n): ")
    if contains_georgian(ans):
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        continue
    if ans.lower() == 'y':
        character_pool += upper_letters
        break
    elif ans.lower() == 'n':
        break

while True:
    ans = input("გსურთ რიცხვები? (y/n): ")
    if contains_georgian(ans):
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        continue
    if ans.lower() == 'y':
        character_pool += digits
        break
    elif ans.lower() == 'n':
        break

while True:
    ans = input("გსურთ სიმბოლოები? (y/n): ")
    if contains_georgian(ans):
        print("შეიყვანე მხოლოდ ლათინური ასოები")
        continue
    if ans.lower() == 'y':
        character_pool += symbols
        break
    elif ans.lower() == 'n':
        break

if character_pool == "":
    print("არცერთი ტიპი არ აგირჩევიათ. ავტომატურად გამოყენებული იქნება პატარა ასოები.")
    character_pool = lower_letters

password_list = []

for _ in range(length):
    random_char = random.choice(character_pool)
    password_list.append(random_char)

generated_password = "".join(password_list)

print(f"თქვენი პაროლია: {generated_password}")

print("დავალება 2 ")

password = input("შეიყვანეთ პაროლი შესაფასებლად: ")

if not password:
    print("პაროლი ცარიელია!")
else:
    score = 0
    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    lower_count = sum(1 for char in password if char.islower())
    upper_count = sum(1 for char in password if char.isupper())
    digit_count = sum(1 for char in password if char.isdigit())

    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>/?"
    symbol_count = sum(1 for char in password if char in special_characters)

    if lower_count >= 1:
        score += 1

    if upper_count >= 1:
        score += 1

    if digit_count >= 2:
        score += 2
    elif digit_count == 1:
        score += 1

    if symbol_count >= 2:
        score += 2
    elif symbol_count == 1:
        score += 1

    if len(set(password)) / length >= 0.8:
        score += 1

    has_consecutive = False
    for i in range(length - 1):
        if password[i] == password[i + 1]:
            has_consecutive = True
            break

    if not has_consecutive:
        score += 1

    if score <= 4:
        strength = "weak"
    elif score <= 7:
        strength = "medium"
    else:
        strength = "strong"

    print(f"ქულა: {score}/10")
    print(f"შეფასება: {strength}")


    print("დავალება 3")


def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


while True:
    user_input = input("შემოიტანეთ ფიბონაჩის რიგის სიგრძე: ")

    if user_input.isdigit():
        length = int(user_input)
        if length > 0:
            break
        else:
            print("გთხოვთ შეიყვანოთ 0-ზე მეტი რიცხვი!")
    else:
        if user_input.strip() == "":
            print("შენ შემოიტანე ცარიელი ტექსტი, არასწორია, მხოლოდ რიცხვი!")
        else:
            print(f"შენ შემოიტანე '{user_input}', ეს არასწორია, მხოლოდ რიცხვი!")

fib_series = generate_fibonacci(length)
print(f"ფიბონაჩის მიმდევრობა {length} ელემენტით: {fib_series}")

print("დავალება 4")

text = input("შეიყვანეთ ტექსტი: ")
cleaned = "".join(char.lower() for char in text if char.isalnum())

if not cleaned:
    print("ტექსტი არ შეიცავს ასოებს ან ციფრებს.")
elif cleaned == cleaned[::-1]:
    print(f"ტექსტი არის პალინდრომი!")
else:
    print(f"ტექსტი არ არის პალინდრომი.")

    L = 0
    R = len(cleaned) - 1
    while L < R and cleaned[L] == cleaned[R]:
        L += 1
        R -= 1

    suggestions = set()


    cand_del_L = cleaned[:L] + cleaned[L + 1:]

    cand_del_R = cleaned[:R] + cleaned[R + 1:]

    cand_ins_L = cleaned[:L] + cleaned[R] + cleaned[L:]

    cand_ins_R = cleaned[:R + 1] + cleaned[L] + cleaned[R + 1:]

    for cand in [cand_del_L, cand_del_R, cand_ins_L, cand_ins_R]:
        if cand == cand[::-1]:
            suggestions.add(cand)

    if suggestions:
        print("ყველაზე ახლო პალინდრომები (1 სიმბოლოს ჩასმით/წაშლით):")
        for s in suggestions:
            print(f"-> {s}")
    else:
        print("მხოლოდ 1 სიმბოლოს ჩასმით/წაშლით პალინდრომი ვერ შეიქმნება.")


print("დავალება 5")
while True:
    user_input = input("შეიყვანეთ მხოლოდ ერთი სიტყვა: ").strip()

    if not user_input:
        print("შეცდომა: ველი ცარიელია.")
        continue

    if len(user_input.split()) != 1:
        print("შეცდომა: შეიყვანეთ მხოლოდ ერთი სიტყვა! (გამოტოვებების გარეშე)")
        continue

    word = user_input
    break

nicknames = [
    f"The_{word}",
    f"{word}_Pro",
    f"Cyber_{word}",
    f"Captain_{word}",
    f"{word}inator"
]

print("\nშემოთავაზებული 5 ზედმეტსახელი:")
for nickname in nicknames:
    print(f"-> {nickname}")


print("დავალება 6")
import random

while True:
    user_input = input("შეიყვანეთ რიცხვები ერთმანეთისგან გამოტოვებით: ").strip()
    try:
        numbers = [int(x) for x in user_input.split()]
        if not numbers:
            print("სია ცარიელია!")
            continue
        break
    except ValueError:
        print("შეცდომა: შეიყვანეთ მხოლოდ რიცხვები!")

print("\nროგორ გსურთ სიის დალაგება?")
print("1. ზრდადობით")
print("2. კლებადობით")
print("3. Random-ად")
print("4. მხოლოდ უნიკალური მონაცემები")

choice = input("აირჩიეთ სასურველი ვარიანტი (1-4): ").strip()

if choice == "1":
    print(f"შედეგი: {sorted(numbers)}")
elif choice == "2":
    print(f"შედეგი: {sorted(numbers, reverse=True)}")
elif choice == "3":
    shuffled_list = numbers.copy()
    random.shuffle(shuffled_list)
    print(f"შედეგი: {shuffled_list}")
elif choice == "4":
    unique_list = list(dict.fromkeys(numbers))
    print(f"შედეგი: {unique_list}")
else:
    print("არასწორი არჩევანი!")

print("დავალება 7")
text = input("შეიყვანეთ ტექსტი: ")

filtered_text = "".join(char for char in text if char.isalpha() or char.isspace())

print(f"გაფილტრული ტექსტი: {filtered_text}")
print("დავალება 8")
user_input = input("შეიყვანეთ რიცხვები (მაგ. 3,5,7,2): ")


cleaned_input = user_input.replace(",", " ")
base_row = [int(x) for x in cleaned_input.split()]

if not base_row:
    print("სია ცარიელია!")
else:
    all_rows = [base_row]


    while len(all_rows[-1]) > 1:
        current_row = all_rows[-1]
        next_row = [current_row[i] + current_row[i+1] for i in range(len(current_row) - 1)]
        all_rows.append(next_row)

    print("\nშედეგი:")
    for row in all_rows:

        print(" ".join(str(x) for x in row))

print("დავალება 9")
text = input("შეიყვანეთ ტექსტი: ")


cleaned_text = ""
for char in text.lower():
    if char.isalnum() or char.isspace():
        cleaned_text += char
    else:
        cleaned_text += " "

words = cleaned_text.split()

if not words:
    print("ტექსტი არ შეიცავს სიტყვებს.")
else:

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1


    max_count = max(word_counts.values())


print("დავალება 10")

text = input("შეიყვანეთ წინადადება: ")

word_lengths = {}
for word in text.split():
    cleaned_word = word.strip(".,!?;:\"'()")
    if cleaned_word:
        word_lengths[cleaned_word] = len(cleaned_word)

print(word_lengths)