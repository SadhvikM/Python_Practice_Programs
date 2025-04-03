import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

# Easy Level -> without shuffling the characters
# password = ""
# for char in range(0, num_letters):
#     password += random.choice(letters)
#
# for char in range(0, num_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, num_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard level -> with shuffling the characters
password_list = []
for char in range(0, num_letters):
    password_list.append(random.choice(letters))

for char in range(0, num_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, num_numbers):
    password_list.append(random.choice(numbers))

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")