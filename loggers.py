def correct_second_name():
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + ".txt", "r", encoding="utf-8")
    print(data.read())
    data.close()

    data = open(file_name + ".txt", "w", encoding="utf-8")
    print("Введите НОВУЮ фамилию: ")
    original_second_name = input()
    data.write(original_second_name)
    data.close()

def correct_name():
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + ".txt", "r", encoding="utf-8")
    print(data.read())
    data.close()

    data = open(file_name + ".txt", "w", encoding="utf-8")
    print("Введите НОВОЕ имя: ")
    original_name = input()
    data.write(original_name)
    data.close()

def correct_surname():
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + ".txt", "r", encoding="utf-8")
    print(data.read())
    data.close()

    data = open(file_name + ".txt", "w", encoding="utf-8")
    print("Введите НОВОЕ отчество: ")
    original_surname = input()
    data.write(original_surname)
    data.close()

def correct_phone():
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + ".txt", "r", encoding="utf-8")
    print(data.read())
    data.close()

    data = open(file_name + ".txt", "w", encoding="utf-8")
    print("Введите НОВЫЙ номер телефона(+7): ")
    original_phone = input()
    data.write(original_phone)
    data.close()


def delete_file():
    print("Введите имя файла: ")
    file_name = input()
    data = open(file_name + ".txt", "r", encoding="utf-8")
    print(data.read())
    data.close()

    import os
    os.remove(file_name + ".txt")
    data.close()


