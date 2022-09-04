from random import randint

cpf = randint(100000000, 999999999)
cpf = str(cpf)
total1 = 0
total2 = 0

for i, n in enumerate(range(10, 1, -1)):
    total1 += int(cpf[i]) * n

digito1 = 11 - (total1 % 11)

if digito1 > 9:
    digito1 = 0

for i, n in enumerate(range(11, 2, -1)):
    total2 += int(cpf[i]) * n
    if n == 3:
        total2 += digito1 * 2

digito2 = 11 - (total2 % 11)

cpf += str(digito1) + str(digito2)

print(cpf)
