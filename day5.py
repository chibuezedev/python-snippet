# fruits = ["apple", "orange", "grape"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " is good")
#     print()


# sum = 0
# student_heights = [181, 124, 165, 173, 189, 169, 146]
# for student_height in student_heights:
#     sum = sum + student_height
#     average = sum / 2
#     if average == float:
#         print(round(average))
# else:
#     print(average)


# # 🚨 Don't change the code below 👇
# highest_score = 0;
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# # Write your code below this row 👇
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f"The highest score in the class is {highest_score}")

#
# total = 0
#
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)


# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     if number % 3 == 0:
#         print(" Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
    random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
    print(f"Your password is {password}")
