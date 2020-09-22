# Name:- Anurag Rai

# CYCLIC REDUNDANCY CHECK (CRC) METHOD FOR DETECTINGERROR IN BIT STREAM

# Division of binary datatype
def division(divident, divisor):
    # print(f"divident: {divident} \t divisor: {divisor}")
    if len(divident) < len(divisor):
        # print(f"remender: {divident}")
        # return 0, divident
        ans = 0
        rem = divident
    else:
        rem = ''
        for (dive, divs) in zip(divident, divisor):
            if dive == divs:
                rem += str(0)
            else:
                rem += str(1)
        ans = 1

    index = 0
    for i in rem:
        if i == '1':
            break
        index += 1
    if rem[index:] == None:
        rem = 0
    else:
        rem = rem[index:]
    # print(f"New rem: {rem}")

    return ans, rem
###########################################################

def newDivi(divident, remainder):
    print("running")
    length = len(remainder)
    carry = 0
    temp1 = ""
    temp2 = ''
    for i in range(1,length+1):
        if int(divident[-i]) + int(remainder[-i]) + int(carry) == 3:
            carry = 1
            temp2 += str(1)
        elif int(divident[-i]) + int(remainder[-i]) + int(carry) == 2:
            carry = 1
            temp2 += str(0)
        elif int(divident[-i]) + int(remainder[-i]) + int(carry) == 1:
            carry = 0
            temp2 += str(1)
        elif int(divident[-i]) + int(remainder[-i]) + int(carry) == 0:
            carry = 0
            temp2 += str(0)
        
        # print(remainder[-i], " ", divident[-i])
        # print(temp2, '\n')


    while (carry == 1):
        if divident[-(length)] + carry == 0:
            break
        elif divident[-(length)] + carry == 1:
            temp1 += str(1)
            carry = 0
        elif divident[-(length)] + carry == 2:
            temp1 += str(0)
            carry = 1
        elif divident[-(length)] + carry == 3:
            temp1 += str(1)
            carry = 1
        length += 1
    l = (len(divident) - len(temp1)) - len(temp2)
    temp1 = divident[:l] + temp1
    # print(temp2)
    temp1 = temp1[::-1]  # reverse the string
    temp2 = temp2[::-1]
    return temp1+temp2




############################################################


msg = input("Enter your message in binary: ")   # Divident
key = input("Enter the key in binary: ")    # Divisor
remainder = 0
quotent = ''

# creating divident with the help of msg and number of digits in key
divident = msg + ('0' * (len(key)-1))
print(f"The divident is: {divident}")
print(f"Divisor is: {key}")

div = divident[0:len(key)]
# print(f"Starting divident: {div}")
for i in range(len(key), len(divident)):
    qut,rem = division(div, key)
    quotent += str(qut)
    div = rem + divident[i]
    # print(f"Quotent is: {quotent}")
    # print('\n\n\n')
    # print(f"New divident: {div}")

rem = div
print(f"Quotent: {quotent}")
print(f"Remainder: {rem}")
newDivident = newDivi(divident, rem)
print(f"New divident or Recived divident is: {newDivident}")


# checking error
rem = ''
div = divident[0:len(key)]
for i in range(len(key), len(newDivident)):
    qut, rem = division(div, key)
    quotent += str(qut)
    div = rem + newDivident[i]
print(f"The new remainder is: {div}")
if int(div) == 0:
    print("No Error")
else:
    print("Error detected")