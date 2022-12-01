import delete
import viev
import edit
import add
import search


def menu():
    while True:
        value= input('Выберите:\n \
             1.-Вывести все записи.\n \
             2.-Добавить запись.\n \
             3.-Найти запись.\n \
             4.-Изменить запись.\n \
             5.-Удалить запись.\n \
             6.-Выход\n')
        if value == "1":
            viev.print_all_to_console()
        elif value == "2":
            add.reading()
        elif value == '3':
            search.Search_Entry('employees.csv')
        elif value == '4':
            edit.Edit_Entry('employees.csv')
        elif value == '5':
            delete.delete_str('employees.csv')
        elif value == '6':
            print('Пока!!!')
            break 
