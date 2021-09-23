# # fuct(a, 6) ->
#
# def num_(a, n):
#     new=[]
#     for i in a:
#         if i > n:
#             new.append(i)
#         else:
#             continue
#     print(new)
#     return(new)
#
# a = [1,2,3,4,4,2,42,34,124,123,12,3,123123,2142345,123123,42423]
#
# num_(a,5)



def srez(a,b):
    res = list(set(a) & set(b))
    print(res)
    return res

a = [1,2,3,4,4,2,42,34,124,123,12,3,123123,2142345,123123,42423]
b = [1,4,5,6,6,7,8,8,8,9,34]

srez(a,b)


#посчитать наиболее часто встречаемые слова в тексе

def text_a(a):
    list_=a.split(" ")
    for i in list_:
        counter = list_.count(i)
        print(i, counter)









a = "Hey Hey little little big big big"

text_a(a)






