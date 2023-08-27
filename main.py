from loggers import correct_second_name, correct_name, correct_surname, correct_phone, delete_file

def main():
    print("Здравствуйте! ")
    print("Вы находитесь в меню справочника")
    print("1 - редактировать фамилию\n"
          "2 - редактировать имя\n"
          "3 - редактировать отчество\n"
          "4 - редактировать телефон\n"
          "5 - удалить файл\n"
          "6 - выйти из программы\n")
    
    while True:
        command = int(input("Введите номер команды (1-6): "))
        if command not in [1, 2, 3, 4, 5, 6]:
            print("Ошибочный запрос!")
        elif command == 1:
            correct_second_name()
        elif command == 2:
            correct_name()
        elif command == 3:
            correct_surname()
        elif command == 4:
            correct_phone()
        elif command == 5:
            delete_file()
            print("Файл удален!")
        elif command == 6:
            print("Всего доброго!")
            return 
    
main()