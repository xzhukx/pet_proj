def factor_dict(num):
    dictat = {}
    result = 1
    for i in range(1,num+1):
        result = result*i
    dictat.update({i: result})
    print(dictat)
    print(result)
    return result

factor_dict(3)
factor_dict(5)
factor_dict(8)

# factor_dict(10)
#
# def factorial(num):
#     result = 1
#     if num in factor_dict(num):
#         return result
#     else:
#         for i in range(1,num+1):
#             result = result*i
#         return result
#
# factorial(6)
