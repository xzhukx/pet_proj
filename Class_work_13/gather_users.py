
class users_app():

    userdict = []

    def __init__(self, nickname, name, surname, sex, age):
        self.nickname = nickname
        self.name = name
        self.surname = surname
        self.sex = sex
        self.age = age

    def add_to_dict(self):
        self.userdict.append(self.nickname, self.name, self.surname, self.sex,self.age)

    def display_userdict(self):
        print(self.userdict)

    def change_user(self):


user_1=users_app(nickname="Pilya",name="Denys",surname="Piliaiev",sex="men",28)
users_app.add_to_dict(user_1)
# user_2=users_app("Piter","Petro","Lahay","men",27)
# users_app.add_to_dict(user_2)
# user_3=users_app("Bulva", "Vasiliy", "Bulba", "men",30)
# users_app.add_to_dict(user_3)


