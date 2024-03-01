programOn = True
# binary expansion is (10010001011010) (1*2^x) + ...
# decimal expansion is (345) (3*2^x) + (4*2^x)  + ...
binaryList = [1, 0] #0o prefix to automatically turn it to octal
bConv = 0

#binaryPower = 0


def conv_binary(bList):
    getLen = len(bList) - 1 # -1 so the power goes to 0
    conversion = 0
    #print(getLen)
    for num in bList:
        # start from first element in list and work backwards to 0
        twoToPwr = 2**getLen
        temp = (num * twoToPwr)
        conversion = conversion + temp
        getLen = getLen - 1
        #binaryPower = binaryPower + 1
    return conversion

def parse(stringOfNums):
    tmpList =[]
    for number in stringOfNums:
        if number == " ":
            pass
        else:
            number = int(number)
            tmpList.append(number)
    return tmpList

def addToBinaryList(binaryList):
    # ask user if they would like to add a bunch of numbers at once or just one
    # then ask them if they would like to add to front or back of list
    numsToAddList = []
    # For multiple numbers at once or one number
    print("EX: [BACK, ..., FRONT]")
    frontOrBack = int(input("""
    1) Add to front 
    2) Add to back: 
    """))
    if frontOrBack == 1:
        #print("EX FORMAT: 1 0 1 0 1 0") can be read with spaces or without 239 = 2, 3, 9
        numbersToAdd = input("Enter the numbers you would like to add : ")
        parsedInput = parse(numbersToAdd)
        for newNum in parsedInput:
            binaryList.append(newNum)
        print(binaryList)
    elif frontOrBack == 2:
        pass
    else:
        print("Please retry and select a valid option")




while programOn:
    usrMenuChoice = int(input("""
    Welcome to the menu please choose an option:
    ============================================
    1) Add binary numbers to list
    2) Convert
    3) Display List and Conversion
    4) Exit Program
                          
    """))
    if usrMenuChoice == 1:
        addToBinaryList(binaryList)
    elif usrMenuChoice == 2:
        bConv = conv_binary(binaryList)
        print("The conversion number is:", bConv)
    elif usrMenuChoice == 3:
        print(f"Your List is: {binaryList} \nThe converstion number is: {bConv}")
    elif usrMenuChoice == 4:
        print("Closing Program...")
        programOn = False
    else:
        print("**Error please choose a valid option")


#conv_binary(binaryList)