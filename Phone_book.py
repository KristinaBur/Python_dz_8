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
        change_contact()
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
    find_info = input("Введите инфорацию, которую хотите найти: ")
    with open(file_path,'r') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)

def change_contact():
    data_str = input("Введите контакт (например, имя): ")
    user_lst = []
    with open("telephon_list.txt", "r", encoding="utf-8") as d:
        lst = d.readlines()
        for line in lst:
            if data_str in line:
                user_lst.append(line)
    print(*user_lst)
    answer = int(input("Введите строчку, которую хотите заменить: "))
    new_contact = input("Введите новый контакт: ") + "\n"
    
    with open("telephon_list.txt", "w", encoding="utf-8") as d:
        for line in lst:
            if user_lst[answer - 1] != line:
                d.write(line)
            else:
                d.write(new_contact)
    print("Готово!")


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