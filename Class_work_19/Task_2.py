#сделать из цифры наибольшее число

numbers = [0, 48, 39, 82, 71, 90]

def bigest_num(list_of_numbers):
    string_num = str()
    for number in list_of_numbers:
        number=str(number)
        string_num += number
    sorted_list = []
    result = str()
    for num in string_num:
        sorted_list += (num)
        sorted_list.sort(reverse=True)
    for i in sorted_list:
        result += i
    print(result)
    return result

bigest_num(numbers)




