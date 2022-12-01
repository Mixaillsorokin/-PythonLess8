
def Edit_Entry(file):

    print(f'Введите элемент имя сотрудника для изменения данных о нём в БД: ')
    name = input()
    lines = []
    
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if not name in line: 
                    lines += line
                    print('Нет такого имени \n' )
                else:
                    line = line.split(", ")
                    print(line)
                    old = int(input('Что хотите заменить?\n \
                        1.- ID. \n \
                        2.-Фамилию. \n \
                        3.-Имя.\n \
                        4.-Отчество.\n \
                        5.-Отдел.\n \
                        6.-Должность.\n'))
                    new = input("На что заменить: ")
                    line[old - 1] = new
                    line = ", ".join(line)
                    lines += line

    with open(file, 'w+', encoding="utf-8") as data:
            data.writelines(lines)
        
    print('Изменение произведено...')
