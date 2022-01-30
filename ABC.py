from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def solve(self):
        pass
    

class laptop(computer):
    def process(self):
        print("Its printing..")
    
    def solve(self):
        print("solving")

class programmer(computer):
    def process(self):
        print("programming..")
    def solve(self):
        print("solving")

class whiteboard(computer):
    
    def process(self):
        print("programming..")
    def solve(self):
        print("solving")
    def write(self,obj):
        print("its writing..")
        obj.solve()

obj = programmer()

wb = whiteboard()
wb.write(obj)