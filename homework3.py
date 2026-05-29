print("დავალება 1")
char = input("შემოიტანე სიმბოლო: ")
if char.lower() in "აეიოუaeiou":
    print(f'"{char}" ხმოვანია')
else:
    print(f'"{char}" თანხმოვანია')

print("\nდავალება 2")
for i in range(10, -1, -1):
    print(i)

print("\nდავალება 3")
import random

lst = [random.randint(1, 20) for _ in range(10)]
print(lst)
sorted_indexed = sorted(enumerate(lst), key=lambda x: x[1], reverse=True)
for idx, (original_idx, val) in enumerate(sorted_indexed[:3], 1):
    print(f"მონაცემი {idx}: {val} (ინდექსი: {original_idx})")

print("\nდავალება 4")
width = 5
height = 2
for _ in range(height):
    print(" ".join(["#"] * width))

print("\nდავალება 5")


def arithmetic_ops(x, y):
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")
    print(f"{x} // {y} = {x // y}")
    print(f"{x} % {y} = {x % y}")


arithmetic_ops(5, 2)

print("\nდავალება 6")


def draw_rectangle(height, width):
    for _ in range(height):
        print(" ".join(["#"] * width))


draw_rectangle(2, 5)

print("\nდავალება 7")


def in_str(text, char):
    count = text.count(char)
    print(f'Character "{char}" in given string: {count} times')


in_str("John and Jane Doe", "J")

print("\nდავალება 8")


def wc(text):
    count = len(text.split())
    print(f"სიტყვების რაოდენობა წინადადებაში შეადგენს {count}-ს.")


wc("რამდენიმე სიტყვა რომლის დათვლასაც ვაპირებთ")

print("\nდავალება 9")
words = ["პითონი", "კომპიუტერი", "პროგრამირება"]
secret_word = random.choice(words)
attempts = 10
guessed_letters = set()
game_over = False

while attempts > 0:
    display_word = "".join([char if char in guessed_letters else "_" for char in secret_word])
    print(f"სიტყვა: {display_word}")
    user_input = input("შეიყვანეთ ასო ან მთლიანი სიტყვა (ან 'exit'): ")

    if user_input == "exit":
        game_over = True
        break

    if user_input == secret_word:
        print("გილოცავ")
        game_over = True
        break
    elif len(user_input) == 1:
        if user_input in secret_word:
            guessed_letters.add(user_input)
            if set(secret_word).issubset(guessed_letters):
                print("გილოცავ")
                game_over = True
                break
        else:
            attempts -= 1
    else:
        attempts -= 1

if attempts == 0 and not game_over:
    print("თქვენ დამარცხდით")

print("\nდავალება 10")
choices = ["მარჯვენა", "მარცხენა"]
won = True
exit_triggered = False

for _ in range(5):
    correct = random.choice(choices)
    user_input = input("მარჯვენა თუ მარცხენა? (ან 'exit'): ")
    if user_input == "exit":
        exit_triggered = True
        break
    if user_input != correct:
        won = False

if not exit_triggered:
    if won:
        print("გამარჯვება")
    else:
        print("შენ დამარცხდი")