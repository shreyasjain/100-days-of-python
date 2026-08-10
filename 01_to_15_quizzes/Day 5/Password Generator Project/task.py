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

result = []

letters_length = len(letters)
symbols_length = len(symbols)
numbers_length = len(numbers)

for _ in range(nr_numbers):
    random_number = random.randint(0, numbers_length - 1)
    result.append(numbers[random_number])

for _ in range(nr_symbols):
    random_number = random.randint(0, symbols_length - 1)
    result.append(symbols[random_number])

for _ in range(nr_letters):
    random_number = random.randint(0, letters_length - 1)
    result.append(letters[random_number])

print(result)
random.shuffle(result)
password = ''
for char in result:
    password += char
print(f'Your password is : {password}')