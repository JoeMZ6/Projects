import random
while True:
    print("roll the dice (y,n):")
    input_char=str(input())
    if input_char =='n'or input_char=='N':
        print("thanks for playing")
        break
    elif input_char=="y" or input_char=='Y':
        die1=random.randint(1,6)
        
        die2=random.randint(1,6)
        print(f'{die1,die2}')
        continue
    else:
        print("invalid choice!")
        
