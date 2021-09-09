class Iterclass:

    def __init__(self, value_list = dict):
        self.value_list = value_list
        self.index = 0

    def __setattr__(self, key, value):
        self.__dict__.keys()

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 0
        key_self = list(self.__dict__.keys())
        if self.index == len(key_self):
            self.index = 1
            raise StopIteration
        return self.value_list[self.index]

iter_claas = Iterclass(value_list={1: "1",2: "2",3: "3",4: "4",5: "5"})


print(next(iter_claas))
print(next(iter_claas))
print(next(iter_claas))
