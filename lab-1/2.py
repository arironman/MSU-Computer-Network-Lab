
# Objective: Implement a program for Checksum and RAC(Row and Column Parity)method for detecting error in bit stream.

import array

def  no_of_one(data):
	num = 0
	for i in data:
		if i == 1:
			num += 1
	if num%2 == 0:
		return 0
	else:
		return 1



first = [[0, 1, 0 , 1],[0, 0, 0 , 0],[0, 0, 0 , 0]]
second =[[0, 0, 0 , 0],[1, 0, 0 , 0],[1, 0, 0 , 0]]
data = []

print("Enter the first matrix: ")
for i in range(0,3):
	for j in range(0,4):
		first[i][j] = int(input(f"Enter the data of send array of index [{i}][{j}]: "))



print("Enter the second matrix: ")
for i in range(0,3):
	for j in range(0,4):
		second[i][j] = int(input(f"Enter the data of send array of index [{i}][{j}]: "))


print("RAC Parity Checking for first array: ")
new_data = []
for i in range(0,3):
        data = []

        for j in range(0,4):
                print(first[i][j], end = " ")
                data.append(first[i][j])
        print(no_of_one(data))
        new_data.append(no_of_one(data))

for i in range(0,4):
        data = []

        for j in range(0,3):
                data.append(first[j][i])
        print(no_of_one(data), end = " ")
print(no_of_one(new_data))
        




print("RAC Parity Checking for second array: ")
new_data = []
for i in range(0,3):
        data = []

        for j in range(0,4):
                print(second[i][j], end = " ")
                data.append(second[i][j])
        print(no_of_one(data))
        new_data.append(no_of_one(data))

for i in range(0,4):
        data = []

        for j in range(0,3):
                data.append(second[j][i])
        print(no_of_one(data), end = " ")
print(no_of_one(new_data))
