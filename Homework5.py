# Задайте переменные разных типов данных:
immutable_var = (2, 3, 'w', 'f')
print(immutable_var)
# Изменение значений переменных:
immutable_var = (2, 3, 'w', 'f')
# Попытка изменить кортеж
# immutable_var ['w'] = 't' # картеж был создан для не меняемых списков.
# Создание изменяемых структур данных:
mutable_list = [2, 3, 'w', 'f']
mutable_list [0] = 7
# mutable_list [3] = 'Modified'
mutable_list.append('Modified')
print(mutable_list)