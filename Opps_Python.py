---------------------------create class-------------------------------
# 1st method
class abc :
    def show():
        print("My firt python class....")
        
abc.show()

#2nd method //using constructor
class abc :
    def show(self):
        print("My firt python class....")
        
obj=abc()
obj.show()


O/P :-
My firt python class....

---------------------------take static input-------------------------------
class abc :
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Welcome..",self.name)
        
obj=abc("Hemali")
obj.show()

O/P :-
Welcome.. Hemali

---------------------------function call in class-------------------------------
class abc :
    
    def show(self):
        print("Welcome..")
        
class xyz(abc):
    def disp(self):
        print("xyz class method..")
        
#obj=abc("Hemali")
obj1=xyz()
obj1.show()
obj1.disp()

O/P :-
Welcome..
xyz class method..

---------------------------function override method-------------------------------

class abc :
    
    def show(self):
        print("Welcome..")
        
class xyz(abc):
    def show(self):
        print("xyz class method..")
        
#obj=abc("Hemali")
obj1=xyz()
obj1.show()

O/P :-
xyz class method..

---------------------------any type object-------------------------------

class abc :
    
    def show(self):
        print("Welcome..")
        
class xyz(abc):
    def show(self):
        print("xyz class method..")
        
#obj=abc("Hemali")
        
obj=any
        
obj1=abc()
obj=obj1
obj.show()

obj2=xyz()
obj=obj2
obj.show()

O/P :-
Welcome..
xyz class method..

---------------------------if condition-------------------------------

class abc :
    
    def show(self):
        print("Welcome..")
        
class xyz(abc):
    def show(self):
        print("xyz class method..")
        
#obj=abc("Hemali")
        
obj=any
a=int(input("Enter a value 0 or 1:"))

if(a==0):
        
    obj1=abc()
    obj=obj1
    obj.show()
if(a==1):   

    obj2=xyz()
    obj=obj2
    obj.show()

O/P :-
1] Enter a value 0 or 1:1
xyz class method..

2] Enter a value 0 or 1:0
Welcome..

---------------------------if condition-------------------------------
