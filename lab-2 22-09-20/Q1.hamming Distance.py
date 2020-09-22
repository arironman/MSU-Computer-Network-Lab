# Name:- Anurag Rai

msg1 = input("Enter the message 1 binary code: ")
msg2 = input("Enter the message 2 binary code: ")

if len(msg1) != len(msg2):
    print("Wrong Input: Both message is having diffrent length")
    exit(0)

length = len(msg2)
result = ''
for index in range(length):
    if msg1[index] == msg2[index]:
        result += str(0)
    else:
        result += str(1)
print(f"The result code after XOR operation: {result}")
# Conuting Number of ones in result will give us hamming distance
hamming_distance = result.count('1')
print(f"The hamming distance of the given strings is: {hamming_distance}")
