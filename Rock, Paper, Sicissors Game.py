import random
options=['r','p','s']

while 1:
    random_choice=random.choice(options)

    user_choice=str(input("Rock, Paper , or Scissors? (r,p,s):"))
    if user_choice!='r' and user_choice!='p' and user_choice!='s':
        print("Please Enter a Valid Choice")

    if user_choice==random_choice:
        print("you and the computer choosed the same option so its ->> DRAW!!🤝")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break

    elif user_choice=='p'and random_choice=='s':
        print("you choosed 📃 and computer choosed ✂️ so you lost 😓")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break

    elif user_choice=='s'and random_choice=='p':
        print("you choosed ✂️ and computer choosed 📃 so you won 😁")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break

    elif user_choice=='r'and random_choice=='s':
        print("you choosed  🚀 and computer choosed  ✂️ so you won 😁")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break

    elif user_choice=='s'and random_choice=='r':
        print("you choosed  ✂️ and computer choosed  🚀 so you lost 😓")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break

    elif user_choice=='p'and random_choice=='r':
        print("you choosed 📃  and computer choosed  🚀 so you won 😁")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break
    elif user_choice=='r'and random_choice=='p':
        print("you choosed  🚀 and computer choosed  📃  so you lost 😓")
        again=input("do you want to play again (y,n)?")
        if again=='y':
            continue
        else:
            break
    
    

    
        

