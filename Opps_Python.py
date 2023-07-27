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

---------------------------take static input-------------------------------
