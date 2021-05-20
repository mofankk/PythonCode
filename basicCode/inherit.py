class Student(object):
    def hello(self):
        print("Hello, Student")


class Mofan(Student):
    def hello(self):
        print("Hello, Mofan")


class Tong(Student):
    def hello(self, a):
        print("Hello, Tong")
        print("hello, are you ok ? %s", a)


t = Tong()
t.hello('mofan')