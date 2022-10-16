src = not False and True or False and not True

 # TODO расписать упрощение выражения
# 1. Первоначально избавляемся от операторов not
# Получаем result = True and True or False and False
# 2. Затем избавляемся от операторов and
# Получаем result = True or False
# 3. Избавляемся от оператора or
# Получаем result = True


result = True  # TODO подставить результат выражения

print(src == result)
