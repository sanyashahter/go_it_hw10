from input_error import input_error
import Classes
ab = Classes.AdressBook()


def hello(*args):
    print('How can I help you ?')
   

def exit(*args):
    print('Good bye!')
    return False

@input_error
def add(text):
    num = text.split(' ')
    print(num)
    name_add = num[1]
    phone_add = num[2]
    name = Classes.Name(name_add)
    phone = Classes.Phone(phone_add)
    rec = Classes.Record(name, phone)
    # ab = Classes.AdressBook()
    ab.add_record(rec)
    print(ab)

# @input_error
# def change(text):
#     num = text.split(' ')
#     if num[1] in phonebook:
#         phonebook[num[1]] = num[2]
#         print(f'Номер телефона {num[1]} изменен  на {num[2]}')
#         print(phonebook)
#     else:
#         print('Такого контакта не существует')

def show_all(*args):
    if 'show all' in args:
       print(ab.show_all())
    else:
        print('----Uknown command----in show all')

def good_bye(*args):
    if 'good bye' in args:
        return False
    else:
        print('---Uknown command--- in good bye')

# @input_error
# def phone(text):
#     num = text.split(' ')
#     if num[1] in phonebook:
#        b = phonebook.get(num[1])
#        print(b)
#     else:
#         print('---Такого контакта не существует---')
