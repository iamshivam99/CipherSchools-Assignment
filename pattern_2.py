n = int(input("Enter the value of No. of rows: "))

alph_num = 65
curr_alph = alph_num

for i in range(alph_num,alph_num + n):
    for j in range(alph_num , i+1):
        print(chr(curr_alph),end = ' ')
        curr_alph += 1
    print('\r')