# Objective: Implement a program that takes bit stream and input and applies even parity scheme on it.

num = int(input("Enter the Unsigned Integer: "))
binary_num = bin(num)
unsigned_binary_num = binary_num[2:]
print(unsigned_binary_num)
str_num = str(unsigned_binary_num)
no_of_one = 0
for i in str_num:
    if i == '1':
        no_of_one += 1 

if no_of_one%2 == 0:
    pass
else:
    str_num = str_num +'1'
    
print(str_num)
