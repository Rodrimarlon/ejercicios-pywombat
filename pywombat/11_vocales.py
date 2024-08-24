
palabra = str(input('Ingresa una palabra/sentencia: '))
vocales = ''

for i in palabra.lower():
    if i == 'a':
        vocales = vocales + i
    elif i == 'e':
        vocales = vocales + i
    elif i == 'i':
        vocales = vocales + i
    elif i == 'o':
        vocales = vocales + i
    elif i == 'u':
        vocales = vocales + i
    else:
        pass
        

print(vocales.lower())

#Solucion de Eduardo 

# vocales = ''
# sentencia = input('Ingresa una palabra/sentencia: ')

# for letra in sentencia.lower():
#     if letra in ['a', 'e', 'i', 'o', 'u']:
#         vocales = vocales + letra
# print(vocales)
