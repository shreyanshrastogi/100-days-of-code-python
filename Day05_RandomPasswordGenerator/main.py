import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=[]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
pass_length=nr_numbers+nr_symbols+nr_letters

while pass_length!=0:
 rand_num=random.randint(0,2)
 if nr_letters!=0 and rand_num==0:
   nr_letters=nr_letters-1
   pass_length=pass_length-1
   password.append(random.choice(letters))
 elif nr_symbols!=0 and rand_num==1:
   nr_symbols=nr_symbols-1
   pass_length=pass_length-1
   password.append(random.choice(symbols))
 elif nr_numbers!=0 and rand_num==2:
   nr_numbers=nr_numbers-1
   pass_length=pass_length-1
   password.append(random.choice(numbers))

for char in password:
    print(char,end='')





