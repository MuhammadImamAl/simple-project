import random

emojis = {
    'r': '💎',
    'p': '📄',
    's': '✂'
}
choices = ('r', 'p', 's')

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
    elif (player == 'r' and cpu == 's') or (player == 'p' and cpu == 'r') or (player == 's' and cpu == 'p'):
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