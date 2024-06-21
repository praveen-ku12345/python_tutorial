class Human:
    def eat(self):
        print("i can eat")
class Male(Human):
    def sleep(self):
        print("i can sleep")
class  Female(Male):
    def work(sel):
        print("i can work")
x=Female()
x.work()
x.eat()
x.sleep()
print(Female.mro())