n = int(input())

if n % 2 != 0:
    print('Weird')
elif n % 2 == 0:
    if n > 1 and n < 5:
        print('Not Werid')
    elif n > 5 and n < 21:
        print('Weird')
    elif n > 20:
        print('Not Weird')

