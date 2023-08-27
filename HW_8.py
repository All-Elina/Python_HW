# Задача 1
# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.

tele01 = ["Петрова"]
tele01 = ' '.join(tele01)
data = open('data01.txt', 'w', encoding = "utf-8")
data.writelines(tele01)
data.close()

tele02 = ["Татьяна"]
tele02 = ' '.join(tele02)
data = open('data02.txt', 'w', encoding = "utf-8")
data.writelines(tele02)
data.close()

tele03 = ["Ивановна"]
tele03 = ' '.join(tele03)
data = open('data03.txt', 'w', encoding = "utf-8")
data.writelines(tele03)
data.close()

tele04 = ["+79991234567"]
tele04 = ' '.join(tele04)
data = open('data04.txt', 'w', encoding = "utf-8")
data.writelines(tele04)
data.close()

    