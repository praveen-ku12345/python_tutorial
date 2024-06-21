#single inheritance.
class Human:
    def __init__(self,num_heart) -> None:
        self.num_eyes=2
        self.num_noes=1
        self.num_heart=num_heart
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def __init__(self,name,heart) -> None:
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("i can flirt")
    def work(self):
        super().eat()
        print(" i can code")
        super().work()
x=Male("parveen",50)
#x.eat()
#x.work()
#x.flirt()
print(x.num_eyes)
print(x.num_heart)