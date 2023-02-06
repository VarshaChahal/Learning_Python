type="animal"

class Animal:
    tricks=[]
    _pri_var="can't access me"
    
    def __init__(self):
       # self.name=name
       pass
    def add_trick(self,trick):
        print("type is "+type)
        self.tricks.append(trick)
    def call_print_trick(self):
        self.__print_trick()  #using name mangling in python, instead of actual private variables
    def print_trick(self):
        print(self.tricks)
        
    __print_trick=print_trick  #private copy of print_trick