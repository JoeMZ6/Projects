import random 

random_number=random.randint(1,100)

while True:

    user_number=int(input('Guess a number between 1 to 100 \n'))

    if type(user_number)!=int or user_number<=0 or user_number>100 :
        print("Please enter a valid number")
    if user_number>random_number:
        print("Lower your expectations")
    elif user_number<random_number:
        print("higher your expectations")
    else:
        print("you got it ,Nice job!")
        break
    
