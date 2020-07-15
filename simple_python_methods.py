#prints a string
def printMe(printString):
    print printString
    return;


#compares two numbers
def compareMe (int1, int2):
    if int1 > int2:
        print("The first number is bigger than the second number")
    elif int2 > int1:
        print("The second number is bigger than the first number")
    else:
        print("The numbers are equal")

#counts the length of a string
def countCharacters(countString):
    count = 0
    for element in countString:
        count += 1
    print("The length of the string you sent is: " + str(count))


#counts number of vowels in a string
def countVowels(countVowelString):
    count = 0
    lowercase = countVowelString.lower()
    for element in lowercase:
        if element == 'a' or element == 'e' or element == 'i' or element == 'o' or element == 'u':
            count += 1
    print("The number of vowels in  the string you sent is: " + str(count))


#swaps the value of two variable
def variableSwap(value1, value2):
    print("Before swap, value1 is: " + str(value1))
    print("Before swap, value2 is: " + str(value2))
    temp = value1
    value1 = value2
    value2 = temp
    print("After swap, value1 is: " + str(value1))
    print("After swap, value2 is: " + str(value2))


#counts digits in a number
def countDigits(countDigitsInt):
    digits = 0
    while countDigitsInt > 0:
        digits = digits + 1
        countDigitsInt = countDigitsInt/10
    print("The number of digits in the number you sent is: " + str(digits))


#finds the nth fibonacci number
def fibSequence(n):
    count = 2
    fibNums = [0, 1]
    while count < n:
        temp = fibNums[count-1] + fibNums[count-2]
        fibNums.append(temp)
        count = count + 1
    print("The " + str(n) + "th fibonacci number is: " + str(fibNums[n-1]))


#reverses a string
def reverseString(toReverse):
    print("The original string is: " + str(toReverse))
    returnString = ""
    for i in toReverse:
        returnString = i + returnString
    print("The reversed string is: " + str(returnString))



#makes change for a dollar amount entered, only allows bills up to $20 to keep myself from having a ton of loops
def cashRegister(money):
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    moneyNoDecimals = money * 100
    while moneyNoDecimals / 2000 >= 1:
        moneyNoDecimals = moneyNoDecimals - 2000
        twenties = twenties + 1
    while moneyNoDecimals / 1000 >= 1:
        moneyNoDecimals = moneyNoDecimals - 1000
        tens = tens + 1
    while moneyNoDecimals / 500 >= 1:
        moneyNoDecimals = moneyNoDecimals - 500
        fives = fives + 1
    while moneyNoDecimals / 100 >= 1:
        moneyNoDecimals = moneyNoDecimals - 100
        ones = ones + 1
    while moneyNoDecimals / 25 >= 1:
        moneyNoDecimals = moneyNoDecimals - 25
        quarters = quarters + 1
    while moneyNoDecimals / 10 >= 1:
        moneyNoDecimals = moneyNoDecimals - 10
        dimes = dimes + 1
    while moneyNoDecimals / 5 >= 1:
        moneyNoDecimals = moneyNoDecimals - 5
        nickels = nickels + 1
    while moneyNoDecimals / 1 >= 1:
        moneyNoDecimals = moneyNoDecimals - 1
        pennies = pennies + 1
        if moneyNoDecimals == 0:
            break
    print("Twenties = " + str(twenties) + ", tens = " + str(tens) + ", fives = " + str(fives) +
          ", ones = " + str(ones) + ", quarters = " + str(quarters) + ", dimes = " + str(dimes)
          + ", nickels = " + str(nickels) + ", pennies = " + str(pennies))


printMe("I'm checking to see if the print function works!")
compareMe(2, 1)
compareMe(1, 2)
compareMe(1, 1)
countCharacters("This is a string I'm using to test my countcharacters function")
countVowels("HEllo world!")
countDigits(1869)
variableSwap(10, 20)
fibSequence(6)
reverseString("I AM GOING TO REVERSE THIS STRING")
cashRegister(12.13)