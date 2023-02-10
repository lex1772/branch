def string_upper(string):
    """Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами"""
    return string.upper()

def upper_2(string):
    '''Функция, которая делает заглавными первые буквы каждого слова в строке'''
    string_list = string.split()
    new_string = []
    for i in string_list:
        new_string.append(i.capitalize())
    return " ".join(new_string)