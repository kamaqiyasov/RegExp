import csv
import os
import re

class PhoneBook():    
    def __init__(self, lastname, fisirtma):
        self.lastname = lastname
        self.firstname = fisirtma
        self.surname = ""
        self.organization = ""
        self.position = ""
        self.phone = ""
        self.email = ""
        
    def merge_info(self, other):
        if not self.surname and other.surname:
            self.surname = other.surname
        if not self.organization and other.organization:
            self.organization = other.organization
        if not self.position and other.position:
            self.position = other.position
        if not self.phone and other.phone:
            self.phone = other.phone
        if not self.email and other.email:
            self.email = other.email
    
    def get_list(self):
        return [self.lastname, self.firstname, self.surname, self.organization, self.position, self.phone, self.email]
    
    def __eq__(self, other):
        if not isinstance(other, PhoneBook):
            return False
        return self.lastname == other.lastname and self.firstname == other.firstname

def format_phone(phone_number):
    regex = r"(\+7|8)\s?\(?(\d{3})\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})(.?)($|\(?(доб.)\s?(\d{4}).?)"
    subst = "+7(\\2)\\3-\\4-\\5\\6\\8\\9"
    return re.sub(regex, subst, phone_number, 0)
    
def main():
    with open(os.path.join(os.getcwd(), "phonebook_raw.csv"), encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 1: выполните пункты 1-3 ДЗ
    #  lastname,firstname,surname,organization,position,phone,email
    phonebooks = []
    header = contacts_list[0]
    for row in contacts_list[1:]:
        fio = " ".join(row[:3]).split()    
        lastname = fio[0]
        firstname = fio[1]
        employee = PhoneBook(lastname, firstname)

        if len(fio) > 2:
            employee.surname = fio[2]
            
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