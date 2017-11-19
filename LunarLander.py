# Joseph Worsfold - jworsf01.
# This is the Lunar Lander game. Developed for a single player
# to play multiple times within specific parameters. These parameters include:
# altitude, velocity, fuel, gravity, constant, and burn.
# See instructions for more details.


def instructions():
    """Tells the user the rules of the game."""
    print('-' * 50 + '\n' + ' ' * 8 + 'WELCOME TO THE LUNAR LANDER GAME\n' +
          '-' * 50 + '\n'
          'You must land on the Moon without crashing.\n'
          'Every turn you\'ll be told your altitude, velocity,\n'
          'and remaining fuel. You must then decide how much\n'
          'fuel to burn. Win by landing (with an altitude\n'
          'of zero or less) at a velocity under 10 metres per\n'
          'second. Try landing under 5 metres per second!')


def play_again(prompt):
    """Asks if the player wants to play again."""
    if prompt == 'y' or prompt == 'Y':
        return True
    elif prompt == 'n' or prompt == 'N':
        print('Thanks for playing!')
        return False
    else:
        return play_again(input('Invalid entry. Try again (y/n): '))


def initial_variables():
    """Creates a list of the initial variables for the game."""
    turn = 0
    altitude = 500.0
    velocity = 0.0
    fuel = 500.0
    gravity = 2.0
    constant = 0.15
    return [turn, altitude, velocity, fuel, gravity, constant]


def scoreboard(turn, altitude, velocity, fuel):
    """Prints the scoreboard whenever it is called."""
    sep = '-' * 50
    print('%s\nTurn: %d\nAltitude: %.1f metres\nVelocity: %.1f metres/second\n'
          'Fuel: %.1f litres\n%s' % (sep, turn, altitude, velocity, fuel, sep))


def fuel_check(fuel):
    """Checks if there is fuel to burn and then asks the player how much."""
    if fuel > 0:
        return float(input('How much fuel do you want to burn?: '))
    else:
        print('You\'re out of fuel')
        return 0


def burn_calc(fuel):
    """Calculates the amount of fuel to burn based on player input."""
    burn = fuel_check(fuel)
    if burn < 0:  # if the player inputs a negative number
        return 0
    elif burn > fuel:  # if the player inputs more fuel than is avaiable
        return fuel
    else:
        return burn


def turn_calc(list):
    """Takes the list of initial variables and calculates the new list."""
    vars = list
    burn = burn_calc(vars[3])
    vars[3] -= burn  # fuel after subtracting burn
    vars[2] += vars[4]  # velocity after adding gravity
    vars[2] -= vars[5] * burn  # veolcity after adding burn * constant
    vars[1] -= vars[2]  # altitude after subtracting velocity
    vars[0] += 1  # turn counter
    return vars


def game_result(turn, altitude, velocity, fuel):
    """Depending on the velocity when landing, return the game result."""
    if 5.0 >= velocity > 0:
        altitude = 0
        print('You\'ve landed safely! You\'re final score is: ')
        scoreboard(turn, altitude, velocity, fuel)
    elif 10.0 >= velocity > 5.0:
        altitude = 0
        print('You\'ve landed hard! You\'re final score is: ')
        scoreboard(turn, altitude, velocity, fuel)
    else:
        print('You\'ve crashed. Creating a %d mile crater.\n%s'
              % (velocity * 0.13, '-' * 50))


def main():
    instructions()
    playing = True
    while playing:
        vars = initial_variables()
        scoreboard(vars[0], vars[1], vars[2], vars[3])
        while vars[1] > 0:
            vars = turn_calc(vars)
            scoreboard(vars[0], vars[1], vars[2], vars[3])
        game_result(vars[0], vars[1], vars[2], vars[3])
        print(' ' * 19 + 'GAME OVER\n' + '-' * 50)
        playing = play_again(input('Would you like to play again? (y/n): '))


if __name__ == '__main__':
    main()
