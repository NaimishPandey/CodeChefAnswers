balance = 2000
w = int(input('Enter the money you want ot withdraw:'))
if w % 5 == 0:
    print('Processing')
    if w >= balance:
        print('Please enter amount less than 2000')
    else:
        print('Amount left is',balance - w - 0.5 )
else:
    print('Please enter amount in multiple of 5')