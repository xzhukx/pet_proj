
class new:
    def __init__(self, a):
        self.a = a
        self.dict = None

    def iter(self):
        _dict = {}
        for i in self.a:
            _dict.update({i: i})
        self.dict =_dict

    def save(self, file_n):
        if self.dict:
            file = open(file_n, "w")
            file.write(str(self.dict))
            file.close()
            print(file_n)

    def read(self, file_n):
        file = open(file_n, "r")
        self.dict = file.read()
        file.close()
        print(self.dict)

obj=new(a=[3,11,23,2,3123,123,12,312,31,23,"adsasd"])
# obj.iter()
# obj.save("new")
obj.read("new")






