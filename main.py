import random

options = ['Rock', 'Paper', 'Scissors']


def play():
    player1 = input('''
                    Welcome to Rock, Paper and Scissors. 
                    Pick an option: Rock, Paper or Scissors: 
                ''').capitalize()
    if (player1 == 'Rock') or (player1 == 'Scissors') or (player1 == 'Paper'):
        CPU = random.choice(options).capitalize()
        print(f'Player({player1}): CPU({CPU})')
        if player1 == CPU:
            print('This is a tie. We go again')
            play()
        if (player1 == 'Rock') and (CPU == 'Scissors'):
            print('You win')
        elif (player1 == 'Scissors') and (CPU == 'Rock'):
            print('CPU wins')
        if (player1 == 'Paper') and (CPU == 'Rock'):
            print('You win')
        elif (player1 == 'Rock') and (CPU == 'Paper'):
            print('CPU wins')
        if (player1 == 'Scissors') and (CPU == 'Paper'):
            print('You win')
        elif (player1 == 'Paper') and (CPU == 'S'):
            print('CPU wins')
    else:
        print('Invalid input. Try again')
        play()


play()
