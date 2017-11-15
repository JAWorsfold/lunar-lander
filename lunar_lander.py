'''Joseph Worsfold - jworsf01.
   This is the Lunar Lander (1.0) game which has been developed to be played
   multiple times within specific parameters. These parameters include the
   following: altitude, velocity, fuel, gravity, constant, burn. Each turn
   the player is asked how much fuel to burn, which will affect the downward
   velocity created by gravity, and this will affect the altitude on the next
   turn. Winners must get to zero or less altitude at a velociy under 10 metres
   per second. Extra points if it's under 5 metres per second.'''

import string


def instructions():
    """Tells the user the rules of the game."""
    print('The instructions')


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
    print('%s\nTurn: %d\nAltitude: %.1f metres' % (sep, turn, altitude))
    print('Velocity: %.1f m/s\nFuel: %.1f litres\n%s' % (velocity, fuel, sep))


def fuel_check(fuel):
    """Checks if there is fuel to burn and then asks the player how much."""
    if fuel > 0:
        # print('Enter an integer or float, or burn will equal 0.')
        return float(input('How much fuel do you want to burn?: '))
    else:
        print('You\'re out of fuel')
        return 0


def burn_calc(fuel):
    """Calculates the amount of fuel to burn based on input."""
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
    vars[3] -= burn  # fuel
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
        print('You\'ve crashed. Creating a %d mile crater.\n' + '-' * 50)


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
