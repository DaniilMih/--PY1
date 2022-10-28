def get_count_char(str_):
    my_dict = {}
    str_ = str_.lower()
    count = 0

    for i in str_:
        if i.isalpha():
            my_dict[i] = my_dict.get(i, count) + 1

    return my_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
