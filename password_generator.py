import random
password_characters = []
numberz = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','£','$','#','%','&','*','?']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
letters_upper = [letter.upper() for letter in letters]
 #below is a much less efficient way of doing the same thing which i did initially:
    #letters_upper_str = str(letters).upper()
    #letters_upper = letters_upper_str.split(',')
    #letters_upper_list = [item.replace("]", '') for item in letters_upper]
    #letters_upper_list = [item.replace("[", '') for item in letters_upper_list]
    #letters_upper_list = [item.replace("'", '') for item in letters_upper_list]
    #letters.extend(letters_upper_list)
letters.extend(letters_upper)
#print(letters)
print("Welcome to the Password Generator!")
num_letters = int(input("How many letters would you like in your password?\t"))
num_symbols = int(input("How many symbols would you like in your password?\t"))
num_numbers = int(input("How many numbers would you like in your password?\t"))

for num in range(0, num_letters):
    letter_choice = random.choice(letters)
    password_characters.append(letter_choice)
for num in range(0, num_symbols):
    symbol_choice = random.choice(symbols)
    password_characters.append(symbol_choice)
for num in range(0, num_numbers):
    number_choice = random.choice(numberz)
    password_characters.append(number_choice)
random.shuffle(password_characters)
password = ''.join([str(char) for char in password_characters])
print(f"Your Password is: {password}")