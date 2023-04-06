# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def change_function():                                      
    change = input('Введите команду: ')                     
    if change == 'a':
        writing_in_file()
    if change == 'b':
        read_file()
    if change == 'c':
        find_file()
    if change == 'd':
        change_file()
    if change == 'e':
        delete_file()


def writing_in_file():
       with open(file_path, 'a') as f:
            f.writelines('\n'+input("Введите ФИО и телефон: "))


def read_file():                           
    with open(file_path, 'r') as f:                         
        for line in f:
            print(line)


def find_file():
    find_info = input()
    with open(file_path,'r') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


# def change_file():
#     find_info = input()
#     new_info = input()
#     with open(file_path,'r+') as f:
#         for line in f:
#             if find_info.casefold() in line.casefold():
#                 if input("Да/Нет: ") == "Да":
#                     lst = (line.strip()).split(' ')
#                     print(lst)
#                 else: continue


def change_file():
    with open(file_path, 'r+', encoding="utf-8") as open_book:
        seach_param = (input('Введите параметр для поиска: ' ).title())
        with open (file_path, 'w', encoding='utf8') as open_book:
            for line in seach_param:
                if seach_param in line:
                    print(line)
                    add_f = (input('Введите фамилию: ' ).title())
                    add_i = (input('Введите Имя: ' ).title())
                    add_tel = (input('Введите телефон: ' ).title())
                    new_line = add_f +' '+add_i +' '+ add_tel + '\n'
                    line = line.replace(line, new_line)
                open_book.writelines(line)


def delete_file():
    with open(file_path, 'r', encoding="utf-8") as f:
        X = input('Введите Имя или Фамилию для удаления: ')
        lines = f.readlines()
        with open(file_path, 'w', encoding="utf-8") as f:
            for line in lines:
                if X in line:
                    print("Строка удалена")
                else:
                    print(line)    
                    f.write(line)


file_path = r'telephon_list.txt'
change_function()