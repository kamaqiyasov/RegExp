class PhoneBook:    
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
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