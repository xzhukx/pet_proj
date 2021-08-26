
class new:
    def __init__(self, a):
        self.a = a
        self.dict = None

    def iter(self):
        _dict = {}
        for i in self.a:
            _dict.update({i: i})
        self.dict =_dict

    def save(self):
        if self.dict:
            file_n = open("new_f", "w")
            file_n.write(str(self.dict))
            file_n.close()
            print(file_n)


obj=new(a=[3,11,23,2,3123,123,12,312,31,23,"adsasd"])
obj.iter()
obj.save()




