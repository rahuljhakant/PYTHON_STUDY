class Person:

    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)

    def say_age(self):
        print('I am', self.age, 'years old')


p = Person('Nikhil', 25)
p.say_hi()
p.say_age()
