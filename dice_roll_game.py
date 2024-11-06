import random


counter = 0
playing = True
while playing:
    roll = input('Roll the dice? (y/n): ').lower()
    if roll == 'y':
        dice = int(input('\nHow many dice you want to roll?: '))
        dice_count = []
        for i in range(dice):
            dice_count.append(random.randint(1, 6))
        # dice_1 = random.randint(1, 6)
        # dice_2 = random.randint(1, 6)
        print(tuple(dice_count))
        counter += 1
        print(f'Counter = {counter}')
    elif roll == 'n':
        print('Thanks for playing!\n')
        playing = False
    else:
        print('Invalid Input\n')