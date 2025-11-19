import csv
import os
import unittest

from main import format_phone, parse_fio

class TestMain(unittest.TestCase):
    
    def setUp(self):
        with open(os.path.join(os.getcwd(), "phonebook_raw.csv"), encoding="utf-8") as f:
            rows = csv.reader(f, delimiter=",")
            contacts_list = list(rows)
            
        self.list_header = contacts_list[0]
        self.test_row = ['Лагунцов Иван', '', '', '', '', '', 'Ivan.Laguntcov@minfin.ru']
        self.test_row2 = ['Лагунцов Иван Алексеевич', '', '', 'Минфин', '', '+7 (495) 913-11-11 (доб. 0792)', '']
        
    def tearDown(self):
        del self.list_header
        del self.test_row
            
    def test_check_phone(self):
        self.assertEqual(format_phone(self.test_row2[-2]), "+7(495)913-11-11 доб.0792")
        self.assertEqual(format_phone(self.test_row[-2]), "")
    
    def test_check_list_header(self):
        test_list = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
        self.assertEqual(self.list_header, test_list)
    
    def test_parse_fio(self):
        lastname, firstname, _ = parse_fio(self.test_row)
        self.assertTrue(lastname == 'Лагунцов')
        self.assertTrue(firstname == 'Иван')