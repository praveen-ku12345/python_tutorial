class Human():
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def sleep(self):
        print("i can sleep")
class Boy(Male):
    def work(self):
        super().work()
        print("i can code")
x=Boy()
x.eat()
x.sleep()
x.work()