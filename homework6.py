import random
import logging

logging.basicConfig(filename='game.log', level=logging.INFO, format='%(message)s')


def task1():
    word = "CODE"

    def char_generator(text):
        for char in text:
            yield char

    gen = char_generator(word)
    for _ in range(len(word)):
        print(next(gen))


def task2():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    user_input = input("შეიყვანე ინდექსი: ")
    if user_input.isdigit():
        idx = int(user_input)
        try:
            print(arr[idx])
        except IndexError:
            pass


def task3():
    def counter(func):
        def wrapper(*args, **kwargs):
            wrapper.count += 1
            print(f"გამოძახება: {wrapper.count}")
            return func(*args, **kwargs)

        wrapper.count = 0
        return wrapper

    @counter
    def say():
        print("Hi")

    say()
    say()


def task4():
    questions = {
        "2+2": 4,
        "3*3": 9,
        "5+5": 10,
        "10-2": 8,
        "6/2": 3
    }
    score = 0
    for q, a in questions.items():
        ans = int(input(f"{q} = "))
        if ans == a:
            score += 10
    logging.info(f"Task4 Score: {score}")
    print(f"ქულა: {score}")


def task5():
    questions = [("5+5", 10), ("2*2", 4), ("10-5", 5), ("3+3", 6), ("8/2", 4)]

    def gen_q():
        for q in questions:
            yield q

    with open("quiz.log", "w") as f:
        for q_text, q_ans in gen_q():
            user_ans = int(input(f"{q_text} = "))
            f.write(f"{q_text}: {user_ans}\n")


def task6():
    choices = ["ქვა", "ბადე", "მაკრატელი"]
    u_score, c_score = 0, 0
    while u_score < 3 and c_score < 3:
        user = input("ქვა/ბადე/მაკრატელი: ")
        comp = random.choice(choices)
        if user == comp:
            logging.info("ფრე")
            continue
        elif (user == "ქვა" and comp == "მაკრატელი") or \
                (user == "ბადე" and comp == "ქვა") or \
                (user == "მაკრატელი" and comp == "ბადე"):
            u_score += 1
            logging.info(f"მოიგე: {user} vs {comp}")
        else:
            c_score += 1
            logging.info(f"წააგე: {user} vs {comp}")
    print(f"{'შენ' if u_score == 3 else 'კომპიუტერმა'} გაიმარჯვა")


def task7():
    def play():
        while True:
            g1, g2 = random.randint(1, 6), random.randint(1, 6)
            if g1 != g2:
                return g1, g2

    while True:
        r1, r2 = play()
        winner = "Gamer 1" if r1 > r2 else "Gamer 2"
        print(f"{winner} მოიგო ({r1} - {r2})")
        if input("კიდევ შანსი? (y/n): ") != 'y':
            break


def task8():
    words = ["ვაშლი", "მსხალი", "ატამი", "ყურძენი", "ბანანი", "საზამთრო", "ალუბალი", "მარწყვი", "ლიმონი", "ფორთოხალი"]
    selected = random.sample(words, 2)
    hints = [w[:-2] for w in selected]

    guessed = 0
    for i in range(2):
        ans = input(f"გამოიცანი სიტყვა: {hints[i]}... : ")
        if ans == selected[i]:
            guessed += 1

    if guessed == 2:
        print("გამარჯვება")
    elif guessed == 1:
        print("50%")
    else:
        print("დამარცხდი")