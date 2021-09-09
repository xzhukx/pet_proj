import json

class drrr():
    MODE_READ="r"
    MODE_WRITE = "w"

    def __init__(self, value: dict):
        self.value = value

    def __str__(self):
        return "file_name_1"

    def serialize(self, value):
        if type(value) == str:
            return eval(value)
        elif type(value) == dict:
            return str(value)

    def write_files(self):
        value = self.serialize(value=self.value)
        file = open(str(self), self.MODE_WRITE)
        file.write(value)
        file.close()
        print(value)
        return value

    def read(self):
        file = open(str(self), self.MODE_READ)
        self.dict = eval(file.read())
        file.close()

class json_write(drrr):

    def serialize_dict(self, value):
        with open(file, "w") as a:
            a.write(json.dumps(value))
            print(a.read())

#
obj = drrr(value={1: "asd", 2:"asdas", 3: "asd"})
# obj.write_files()
# obj.read()

obj.json_write(value)