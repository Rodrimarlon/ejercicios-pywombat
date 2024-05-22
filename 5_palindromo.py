def palindromo(string):
    if string == string[::-1]:
        print(True)
    else:
        print(False)


palindromo('anitalavalatina')
