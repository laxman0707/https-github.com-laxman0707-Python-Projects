rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choice=[rock,paper,scissors]
user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
a=user_input
if a>=3 or a<0:
  print("invalid number")
else:
 print(choice[int(user_input)])
 a=int(user_input) 

 b=random.randint(0,2)
 print("computer's choice")
 print(choice[b])

 if a==0 and  b==2:
  print("you wins")
 elif b>a:
  print("Computer wins")
 elif a>b:
  print("you wins")
 elif a==b:
  print("Its a draw")
 elif b==0 and a==2:
  print("you loose")
 elif a>=3 or a<0:
  print("invalid number")




