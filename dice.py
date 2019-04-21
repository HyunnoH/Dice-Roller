import random 

number = int(input('Input dice number that you wanna roll: '))

while True:
    print('Dice rolled, Number is: %d' % random.randint(1,number))

    state = input('Roll again? :').lower()
    if state == 'n':
        print('See you again!')
        exit(0)
    elif state == 'y':
        continue

