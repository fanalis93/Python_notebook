import os
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("hello my name is " + self.name)

p1 = Person('John',36)
print(p1.name,p1.age,sep='\n')
p1.age = 40 #modifying object value
print(p1.name,p1.age,sep='\n')

#del p1.age #deletes corresponding property from the object
#del p1 #deletes the object
p1.myfunc()