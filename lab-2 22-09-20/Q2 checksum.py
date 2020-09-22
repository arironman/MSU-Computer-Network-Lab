# Name:- Anurag Rai

msg1 = input("Enter Message 1 in binary code: ")
msg2 = input("Enter Message 2 in binary code: ")
carry = 0
sum = ''
compliment_bin = ""
if len(msg1) != len(msg2):
     print("Invalid Binary message")
     exit(0)

length_msg = len(msg1)
for i in range(length_msg):
    temp = int(msg1[i]) + int(msg2[i]) + carry
    if temp == 0:
        sum += str(temp)
        carry = 0
    elif temp == 1:
        sum += str(1)
        carry = 0
    elif temp == 2:
        sum += str(0)
        carry = 1
    elif temp == 3:
        sum += str(1)
        carry = 1
    else: 
        print(f"Invalid credential at index {i}")

if carry == 1:
    sum += str(1)
print(f"The sum of binary message is: {sum}")

for i in sum:
    if int(i) == 0:
        compliment_bin += str(1)
    else:
        compliment_bin += str(0)


print(f"The checksum of messages is: {compliment_bin}")
