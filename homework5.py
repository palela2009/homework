import itertools
import datetime
import calendar
import random
import time

# 1
word = "ABCD"
perms = list(itertools.permutations(word))
print(f"რაოდენობა: {len(perms)}")
print(perms)

# 2
today = datetime.date.today()
next_tuesday = today + datetime.timedelta(days=(1 - today.weekday()) % 7 + 7)
print(next_tuesday)

# 3
myinput = int(input())
print(calendar.isleap(myinput))

# 4
today = datetime.date.today()
new_year = datetime.date(today.year + 1, 1, 1)
print((new_year - today).days // 7)

# 5
print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))

# 6
chars = "XYZ"
res = []
for i in range(1, 4):
    res.extend([''.join(p) for p in itertools.combinations(chars, i)])
print(res)

# 7
target = random.randint(1, 20)
start_time = time.time()
guess = int(input())
if time.time() - start_time <= 5 and guess == target:
    print("გამარჯვება")
else:
    print("დრო ამოიწურა, თქვენ დამარცხდით")

# 8
start = datetime.datetime.now()
player1 = start + datetime.timedelta(seconds=random.randint(5, 20))
player2 = start + datetime.timedelta(seconds=random.randint(5, 20))
if player1 < player2:
    print("Player 1")
else:
    print("Player 2")

# 9
birthday = datetime.date(2000, 12, 10)
today = datetime.date.today()
next_bday = datetime.date(today.year, birthday.month, birthday.day)
if next_bday < today:
    next_bday = datetime.date(today.year + 1, birthday.month, birthday.day)
print((next_bday - today).days)

# 10
target_pass = [random.randint(1, 6) for _ in range(4)]
while True:
    guess = [random.randint(1, 6) for _ in range(4)]
    print(guess)
    if guess == target_pass:
        print("პაროლი სწორია, საცავი გახსნილია")
        break