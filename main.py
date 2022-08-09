class PrivateExc(Exception):
    pass

class Privacy:
    def __setattr__(self, key, value): # Вызывается для self.key = value
        if key in self.privates:
            raise PrivateExc(key, self) # Сгенерировать определяемые пользователем исключение
        else:
            self.__dict__[key] = value # Избежать зацикливания, ичпользуя ключ словаря

class Test1(Privacy):
    privates = ["age"]

class Test2(Privacy):
    privates = ["name", "pay"]

    def __init__(self):
        self.__dict__["name"] = "Tom"


if __name__ == "__main__":
    X = Test1()
    Y = Test2()
    X.name = "Bob" # Работает
    # Y.name = "Sue" # Терпит неудачу
    print(X.name)

    # X.age = 40 # Терпит неудачу
    Y.age = 40 # Работает
    print(Y.age)