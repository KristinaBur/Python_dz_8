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


def change_file():
    find_info = input()
    new_info = input()
    with open(file_path,'r+') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input("Да/Нет") == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else: continue



# def main():
#     find_file()

file_path = r'telephon_list.txt'
change_function()