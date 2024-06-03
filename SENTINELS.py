#topic: SENTINELS (LOOP TEMRINATION WITH A SPECIFIC VALUE)
number = 2
while number != -1: # Loop until user enters -1 #while loop so it continues until -1
    number = int(input('Enter a number: (or -1 to quit): ')) #input statements that leads to value for variable number
if number != -1:
    print(f'you entered: {number}')

