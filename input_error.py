
import re
def input_error(func):
    def de_corator(text):
        text_list = text.split(' ')
        
        if len(text_list) == 3:
            try:
                pattern = r'^(add|change) [a-zA-Z]{3,} \+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,4}$'
                if bool(re.match(pattern, text)) == True:
                    counter = 1
                else:
                    counter = 0
                1/counter
            except Exception:
                print('LEN = 3 TEXT INPUT ERROR')
            else:
                print('len = 3 текст прошел проверку декоратором')
                return func(text)
        elif len(text_list) == 2:
            try:
                pattern = r'phone [a-zA-Z]{3,}'
                if bool(re.match(pattern, text)) == True:
                    counter = 1
                else:
                    counter = 0
                1/counter
            except Exception:
                print('LEN = 2 TEXT INPUT ERROR')
            else:
                print('len = 2 текст прошет проверку декоратором')
                return func(text)
        elif len(text_list) != 2 or 3:
            print('----LEN INPUT ERROR----')
    return de_corator


