import random
score=1
while True:
    
    random_choice=random.randint(1,6)
    score*=random_choice
    if random_choice==1:
        print(f'you got {random_choice} so your score now is 1 😓')
        score=1

    else:
        print(f"you got {random_choice} so your new score is {score} 🥳 ")
    if score>=500:
        print("congratulations you won 🥳 ")
    else:
        diff=500-score
        print(f"you still need {diff} points to win ")
    choice=input('do you want to continue (y,n)?🤔\n')
    if choice=='y':
        continue
    else: 
        print('thanks for playing 😘')

        break


    