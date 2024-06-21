import random
user_choice=int(input("enter the your choice:Type 0 for Rock,1 for Paper,2 for Scissors:"))
computer_choice=random.randint(0,2)
print("Computer choice")
print(computer_choice)
if computer_choice==0 and user_choice==1:
    print("computer wins")
elif computer_choice==0 and user_choice==2:
    print("user wins")
elif computer_choice==1 and user_choice==0:
    print("user wins")
elif computer_choice==1 and user_choice==2:
    print("user wins")
elif computer_choice==2 and user_choice==1:
    print("computer wins")
elif computer_choice==2 and user_choice==0:
    print("computer wins")
else:
    print("its a draw")