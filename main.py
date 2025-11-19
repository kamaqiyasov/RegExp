import csv
import os
import re

from phonebook import PhoneBook

def format_phone(phone_number):
    regex = r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})(.?)($|\(?(доб.)\s?(\d{4}).?)"
    subst = "+7(\\2)\\3-\\4-\\5\\6\\8\\9"
    return re.sub(regex, subst, phone_number, 0)

def parse_fio(row: list) -> tuple[str, str, str]:
    fio_text = " ".join(row[:3]).strip() 
    if not fio_text:
        return "", "", ""
    
    fio_parts = fio_text.split()
    while len(fio_parts) < 3:
        fio_parts.append("")
    
    return fio_parts[0], fio_parts[1], fio_parts[2] 
        
def main():
    with open(os.path.join(os.getcwd(), "phonebook_raw.csv"), encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 1: выполните пункты 1-3 ДЗ
    #  lastname,firstname,surname,organization,position,phone,email
    phonebooks = []
    header = contacts_list[0]
    for row in contacts_list[1:]:
        
        lastname, firstname, surname = parse_fio(row)  
        employee = PhoneBook(lastname, firstname)
        employee.surname = surname
        
        employee.organization = row[3]
        employee.position = row[4]
        employee.phone = format_phone(row[5])
        employee.email = row[6]
        
        employee_exist = None
        for phonebook in phonebooks:
            if employee == phonebook:
                employee_exist = phonebook
                break
            
        if employee_exist:
            employee_exist.merge_info(employee)
        else:
            phonebooks.append(employee)        
        
    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open(os.path.join(os.getcwd(), "phonebook.csv"), "w", newline='', encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerow(header)
        for phonebook in phonebooks:
            datawriter.writerow(phonebook.get_list())
        
if __name__ == "__main__":
    main()