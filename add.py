def reading():
    cont = [0] * 7
    cont[0] = input('Введите ID: ')
    cont[1] = input('Введите фамилию: ')
    cont[2] = input('Введите имя: ')
    cont[3] = input('Введите отчество: ')
    cont[4] = input('Введите номер телефона: ')
    cont[5] = input('Введите отдел: ')
    cont[6] = input('Введите должность: ')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f'{cont[0]}, {cont[1]}, {cont[2]}, {cont[3]}, {cont[4]}, {cont[5]}, {cont[6]};\n')
    print('Контакт успешно добавлен!')
    