import string

def cod(message, cod):
    alpha = (list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits))
    res = ""
    for i in message:
        if i in alpha:
            index = alpha.index(i)
            res = res + alpha[index+cod]
        else:
            res = res + " "
    print(res)
    return res


message = "When in the chronicle of wasted time" \
       "I see descriptions of the fairest wights," \
       "And beauty making beautiful old rhyme" \
       "In praise of ladies dead, and lovely knights," \
       "Then, in the blazon of sweet beauty’s best," \
       "Of hand, of foot, of lip, of eye, of brow," \
       "I see their antique pen wouyd have express’d" \

cod(mess, 3)