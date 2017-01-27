from weakref import WeakKeyDictionary
class MyDescriptor(object):
    def __init__(self,age):
        self.__age = WeakKeyDictionary()

    def __set__(self, instance, value):

        if not isinstance(value,int):
            raise TypeError('Age must be an int')
        if value < 0 or value > 120:
            raise ValueError('Age cant be negative')

        self.__age[instance] = value

    def __get__(self, instance, value):
        return self.__age[instance]

    def __delete__(self,instance):
        del self.__age[instance]

class Person():
    age = MyDescriptor(object)

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '{0} is {1} years old'.format(self.name,self.age)


obj1 = Person('Satya',40)
print(str(obj1))

obj2 = Person('Tinki',5)
print(str(obj2))

#obj1 = Person('Satya',40)
print(str(obj1))

