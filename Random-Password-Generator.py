import random # Imports the random module to enable randomized choices and shuffling

# Define the character sets available for generating the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Collect user input for the exact count of letters, symbols, and numbers they want
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store the generated characters as a sequence
pw_list = []
# Initialize an empty string that will eventually hold the final password
password = ""

# Loop to randomly pick the requested number of letters and append them to the list
for i in range(nr_letters):
    pw_list.append(random.choice(letters))

# Loop to randomly pick the requested number of symbols and append them to the list
for j in range(nr_symbols):
    pw_list.append(random.choice(symbols))

# Loop to randomly pick the requested number of numbers and append them to the list
for k in range(nr_numbers):
    pw_list.append(random.choice(numbers))

# Print the ordered list (will show all letters, then all symbols, then all numbers)
print(pw_list)

# Shuffle the items inside the list to randomize the character sequence
random.shuffle(pw_list)

# Print the list again to show the newly randomized order
print(pw_list)

# Loop through the shuffled list and concatenate each item to the password string
for pw in pw_list:
    password += pw

# Output the final string to the user
print(password)
