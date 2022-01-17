#Написать функции которые выполняют следующую логику
# f_n = 3
# Func(5,  f_n) -> n + nn + nnn = 615
# n = 5
# 5+55+555=615
# f_n = 4
# Func(5,  f_n) -> n + nn + nnn + nnnn = 6170
# ________________________________

def add(n, f_n):
    n = str(n)
    result = str()
    list_sum = []
    for num in range(f_n):
        result = n+result
        list_sum.append(result)

    sum_of_string = 0

    for str_num in list_sum:
        str_num = int(str_num)
        sum_of_string += str_num
    print(sum_of_string)
    return sum_of_string

add(5, 4)

# ________________________________

# Раздница двух массивов (Уникальные значения)
# Func([1,3,4], [2,4,5]) -> [2, 3, 5]
# Func([1,2,3], [2,4,5]) -> [3, 5]

def diff(a,b):
    result = []
    for num in list(a+b):
        if num not in result:
            result.append(num)
    print(result)
    return result
diff([1,2,3], [2,4,5])

# скорее всего, я не совсем понял условие, в первом случае число "1" уникально, но мы его выкидываем. Во втором число "4 и 1 уникально"
#второе возмозможное решение через set: list(set(b)-set(a)), но результат в обоих случаях не тот который в условии ????

#_________________________

# Находит с троке числа и добавляет их
# Func('as123sdasdasd asa sd 5 asdasd 42 234') - > 123+5+42+234
# Func('as1sd3asd44asd asa sd 5 asd 43') - > 1+3+44+5+43

import re
def find_n(text):
    result = re.findall('\d+', text)
    print(result)

find_n('as123sdasdasd asa sd 5 asdasd 42 234')


# Найдите три ключа с самыми высокими значениями в словаре _dict = {'1key':123, '2key':9785, '3key': 560, '4key':234, '5key': 3451}.

