from collections import UserDict

class Field:
    def __init__(self) -> None:
        pass

class AdressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    # def del_record(self, record):
    #     if record in self.data:
    #         del self.data[record]

    def show_all(self):
        for name, record in self.data.items():
            print(f"{name}")
            print(f"{record}")
            print()  

    def __str__(self):
        return f'AdressBOOK = {str(self.data)}'
    
class Name(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
      
    def __repr__(self):
        return f'Имя  === {str(self.value)}'
    

class Phone(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'Телефон = {self.value}'


class Record():                                   
    def __init__(self, name, phone):
        self.name = Name(name)
        self.phone = Phone(phone)
        self.phones = []
    
    def add_phone(self, phone):
        phone = Phone(phone)
        self.phones.append(phone)
        print(f"Телефон {phone} добавлен в список телефонов")
    
    def edit_phone(self, old_phone, new_phone):
        for i in self.phones:
            if i == old_phone:
                index = self.phones.index(old_phone)
                self.phones[index] = new_phone
                print(f"Старый номер телефона {old_phone} заменено на новый {new_phone}")

    def del_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print("Такого телефона не существует")

    def __repr__(self):
        return f'Данные о учетной записи :  ({repr(self.name)}, {repr(self.phone)})'   

# res_name = str(add_classes_1(['', "Bill", "0962893087"]))
# res_phone = str(add_classes_2(['', "Bill", "0962893087"]))
# print(res_name, res_phone)
# name = Name(res_name)
# phone = Phone(res_phone)
# rec = Record(name, phone)
# ab = AdressBook()
# ab.add_record(rec)
# print(ab)

# # text = ['', "Bill", "0962893087"]

 # def __repr__(self):
    #     phone_strings = ', '.join([str(phone) for phone in self.phones])
    #     return f'Name - {str(self.name)}  Запись - {phone_strings}'