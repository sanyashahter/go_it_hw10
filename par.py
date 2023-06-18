from handler import hello, exit, add, show_all, good_bye

def par(text):
    text_list = text.split(' ')
    if text_list[0] in commands:
        func = commands[text_list[0]]
        return func(text)
    else:
        print('-----Unknown command-----')

commands = {'hello':hello,
            'add':add,
            # 'change':change,
            # 'phone':phone,
            'show':show_all,
            'exit':exit,
            'close':exit,
            'good':good_bye
            }

