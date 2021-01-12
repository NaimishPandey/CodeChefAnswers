testcases = int(input('Enter the number of test cases'))
myresult = 0
for i in range(testcases):
    myinput= int(input("Enter the number"))
    for j in range(1,myinput):
        g = myinput%10
        myresult = myresult + g
        myinput = int(myinput/10)

print(myresult)