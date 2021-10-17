sum = 0
while(True):
    userinput = int(input("Enter the price of a item or press q to quit: \n "))
    if(userinput!='q'):

        sum = sum + int(userinput)
        print((f"oder is so far: {sum}...."))
    else:
        print(f"Your Toatal Bill is {sum}. Thank you Visit Again")
        break

        print(sum)