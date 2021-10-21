text_ = "asda sd as.dasdasdasdasdadsasaasdasdasdasdad Plese help asdasdasda asdasdas STOPaaaaaaaaa . as Plese help das das. ad asd a sdads asdf asdf. asdfas dfasdf asdfasdf asd fasdf. helpasd asd fas df asd fasd fjhsajkasdf" \
       "asdnasd,asmd Plese ,asdasmd, Plese help asadas dads. a dsas dasd. asdasdasdadsda  Plese help asdasasdas asd asda d asd asda da dad asd ada sd  asd ads asddasdasdasdasdaf asdfasdfasdfasdfasdfasdf" \
        "asdfa sdfas  fasdfasdfasdasd fasdfasdfads. asdasdasdasdasdasdd .asd. helpwww. adasdasdashelp"

def finder(text, word, length):
    if text.find(word):
        list_=text.split(".")
        result = []
        for sentense in list_:
            if word in sentense:
                if len(sentense) < length:
                    result.append(sentense)
                else:
                    result.append("..." + sentense[sentense.find(word):(sentense.find(word)+length)] + "...")
            else:
                continue
        print(result)
        return result

finder(text_, "help", 30)