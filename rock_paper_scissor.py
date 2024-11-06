import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'

emojis = {
    'r': '💎',
    'p': '📄',
    's': '✂'
}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        player = input('\nRock, paper or scissor, (r/p/s)?: ').lower()
        if player in choices:
            return player
        else:
            print('Invalid choice!')

def displaying_choice(player, cpu):
    print(f'{emojis[player]}')
    print(f'{emojis[cpu]}')

def determine_winner(player, cpu):
    if player == cpu:
        print('Tie!')
    elif (player == ROCK and cpu == SCISSOR) or (player == PAPER and cpu == ROCK) or (player == SCISSOR and cpu == PAPER):
        print('You win!')
    else:
        print('You lose.')

def play_game():
    while True:
        player = get_user_choice()
        
        cpu = random.choice(choices)

        displaying_choice(player, cpu)
        
        determine_winner(player, cpu)
        
        
        replay = input('\nYou want to play again? (y/n): ').lower()
        if replay == 'y':
            continue
        else:
            break

play_game()