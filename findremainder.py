testcases = int(input('Enter the number of test case:'))
for i in range(testcases):
    dividend = int(input("Enter the dividend number:"))
    divisor = int(input('Enter the divisor number:'))
    rem = dividend % divisor
    print("The remainder is", rem)