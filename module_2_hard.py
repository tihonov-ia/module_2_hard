print('"Ребус Индианы Джонса"')
def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result

number = 0
while number < 3 or number > 20:
    number = int(input('Укажите число на первом камне от 3 до 20: '))

password = generate_password(number)
print(f' {number}: {password} - нужный пароль')
print('Выход из ловушки')