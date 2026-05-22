import random

secret_number = random.randint(0, 50)
attempts = 0

print("თამაში: გამოიცანი რიცხვი 0-დან 51-მდე!")
print("თამაშიდან გასასვლელად ჩაწერეთ: exit")

while True:
    user_input = input("შეიყვანეთ რიცხვი: ")

    if user_input.lower() == 'exit':
        print("თამაში შეწყდა")
        break

    if not user_input.isdigit():
        print("შეიყვანეთ მხოლოდ დადებითი რიცხვი")
        continue

    guess = int(user_input)

    if guess < 0 or guess >= 51:
        print(" რიცხვი სცდება არეალს")
        continue

    attempts += 1

    if guess == secret_number:
        print(f"გამოიცანი {secret_number} რიცხვი, მცდელობა: {attempts}")
        break
    elif guess < secret_number:
        print(" ჩემი რიცხვი უფრო დიდია, სცადეთ თავიდან")
    else:
        print(" ჩემი რიცხვი უფრო პატარაა, სცადეთ თავიდან")