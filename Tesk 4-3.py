#3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии
# тех студентов, которые имеют средний балл более «4».
#Нужно перезаписать файл.
#Пример:
#Ангела Меркель 5
#Андрей Валетов 5
#Фредди Меркури 3
#Анастасия Пономарева 4

#Программа выдаст:
#АНГЕЛА МЕРКЕЛЬ 5
#АНДРЕЙ ВАЛЕТОВ 5
#Фредди Меркури 3
#Анастасия Пономарева 4
import re
with open('imput_Task_3.txt', 'w',encoding='utf-8') as file:
    file.write('Ангела Меркель 5\nАндрей Валетов 5\nФредди Меркури 3\nАнастасия Пономарева 4\n')
with open('imput_Task_3.txt', 'r',encoding='utf-8') as file:
    data = file.read().split('\n')
if len(data[-1]) == 0:
    data.pop(-1)
for i in range(0,len(data)):
    res = re.findall(r'5', data[i])
    if '5' in res:
        data[i] = str(data[i]).upper()
with open('imput_Task_3.txt', 'w',encoding='utf-8') as file:
    for i in data:
        file.write(i)
        file.write('\n')