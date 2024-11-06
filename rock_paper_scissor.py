import random

emojis = {
    'r': '💎',
    'p': '📄',
    's': '✂'
}
choices = ('r', 'p', 's')
while True:
    player = input('\nRock, paper or scissor, (r/p/s)?: ').lower()
    cpu = random.choice(choices)
    if player not in choices:
        print('Invalid choices!')
        continue
    
    print(f'{emojis[player]}')
    print(f'{emojis[cpu]}')
    if player == cpu:
        print('Tie!')
    elif (player == 'r' and cpu == 's') or (player == 'p' and cpu == 'r') or (player == 's' and cpu == 'p'):
        print('You win!')
    else:
        print('You lose.')
    
    replay = input('\nYou want to play again? (y/n): ').lower()
    if replay == 'y':
        continue
    else:
        break