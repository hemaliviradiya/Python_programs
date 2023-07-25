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
