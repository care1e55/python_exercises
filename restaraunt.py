MENU = {
    "tea": 1.50,
    "chiken": 3.00,
    "falaphel": 2.00,
    "cheese plate": 5.00,
    "burger": 2.50,
    "shrimps": 5.00
}

total = 0

while True:
    order = input("Order: ").strip().lower()
    if not order:
        print(f"Your total is {total}")
        break
    try:
        current_price = MENU[order]
    except:
        print(f"Sorry, we are fresh ou of {order} today")
        continue
    total += current_price
    print(f"{order} costs {current_price}, total is {total}")
