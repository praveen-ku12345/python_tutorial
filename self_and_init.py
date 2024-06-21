#init method is used to initialise objects ,to initialize data members of class while creating the object.
#init method is called everytime you create object
#Self is a keyboard and it is used to binding the object attributes to the arguments received
class Instructor:
    def __init__(self,name_of,address_of):
        self.name=name_of
        self.address=address_of
    def display(self,subject):
        print(f"hii i am {self.name} and i teach {subject}")        
x=Instructor("Praveen","telangana")
print(x.name,x.address)
x.display("python")