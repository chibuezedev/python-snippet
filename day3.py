print("Welcome to python pizza deliveries.")
size = input("What Size of pizza do you want? S, M, L?").lower()
add_pepperoni = input("Do you want Pepperoni? Y or N").lower()
extra_cheese = input("do you want extra cheese? Y or N").lower()
price = 0

if size == "s":
    print(f"The price of a small pizza is $15")
    price = 15
    if add_pepperoni == "y":
        price += 2
        if extra_cheese == "y":
            price += 1

elif size == "l":
    price = 20
    print(f"The price of a medium pizza is ${price}")
    if add_pepperoni == "y":
        price += 3
        if extra_cheese == "y":
            price += 1
elif size == "l":
    price = 25
    print(f"The price of a large pizza is ${price}")
    if add_pepperoni == "y":
        price = 3
        if extra_cheese == "y":
            price += 1

else:
    print(f"The price of your pizza is {price}")
