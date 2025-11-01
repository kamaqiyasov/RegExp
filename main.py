from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import os

with open(os.path.join(os.getcwd(), "phonebook_raw.csv"), encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
#  lastname,firstname,surname,organization,position,phone,email
new_list = []
for row in contacts_list:
    fio = []
    fio.extend([row[0], row[2], row[2]])
    print(" ".join(fio))


# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)