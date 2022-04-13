def convert_num_decimal(num_binary):
    num_decimal = int(num_binary, base=2)
    return num_decimal


num_binary = input('Número binario: ')
num_decimal = convert_num_decimal(num_binary)

print('Número decimal: ' + str(num_decimal))
