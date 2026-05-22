products = {
    "რაკეტა": 15000,
    "ხომალდი": 25000,
    "ჩაფხუტი": 5000
}
cart = []
total_price = 0
print("გამარჯობა! თქვენ იმყოფებით მაღაზია SpaceX-ში.")
print("ჩვენი პროდუქტებია:")
for prod, price in products.items():
    print(f" - {prod}: {price}$")
print("შეიყვანეთ ნივთების სახელები სათითაოდ.")
print("როცა მორჩებით, ჩაწერეთ: დასრულება")
while True:
    choice = input("შეიყვანეთ სასურველი ნივთის სახელი: ")
    if choice == 'დასრულება':
        break
    elif choice in products:
        cart.append(choice)
        total_price += products[choice]
        print(f"✓ {choice} დაემატა კალათაში. მიმდინარე ჯამი: {total_price}$")
    else:
        print(" ასეთი ნივთი  არ არის.")

if total_price == 0:
    print("თქვენ არაფერი აგირჩევიათ")
else:
    print(f"თქვენი კალათა: {cart}")
    print(f"საბოლოო ჯამური ღირებულება: {total_price}$")

    confirm = input("გსურთ ნივთების შეძენა? (კი / არა): ")

    if confirm == 'კი':
        print("ნივთები წარმატებით შეიძინეთ")
    else:
        print("მუშაობა დასრულებულია")


