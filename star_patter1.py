n = int(input("Enter the value of No. of rows: "))
count = 0

for i in range(n):
    count = i + 1
    for j in reversed(range(n)):
        
        if (count > 0) & (j <= i):
            print(' *', end = '')
            count -= 1
        else:
            print(' ',end = ' ')
    print('\r')