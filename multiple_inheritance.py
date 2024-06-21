class Human:
    def __init__(self,language) -> None:
        print("calling init from human")
        self.num_eyes=2
        self.num_noes=1
        self.language=language
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male:
    def __init__(self,name) -> None:
        print("calling init from male")
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        print("i can code ")
class Boy(Human,Male):#mro(method resolution order)
    def __init__(self,name,heart,language) -> None:
        Human.__init__(self,language)
        Male.__init__(self,name)
        self.heart=heart
    def work(self):
        print("hii")
    def display(self):
        print(f"hi iam {self.name} and i work on {self.language}")
x=Boy("Praveen",1,"python")
# x.work()
# x.flirt()
# x.eat()
# Male.work(x)
# print(Boy.mro())
print(x.num_eyes)
print(x.name)
print(x.language)
x.display()