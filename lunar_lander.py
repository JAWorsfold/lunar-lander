'''Joseph Worsfold - jworsf01.
   This is the Lunar Lander (1.0) game which has been developed to be played
   multiple times within specific parameters. These parameters include the
   following: altitude, velocity, fuel, gravity, constant, burn. Each turn
   the player is asked how much fuel to burn, which will affect the downward
   velocity created by gravity, and this will affect the altitude on the next
   turn. Winners must get to zero or less altitude at a velociy under 10 metres
   per second. Extra points if it's under 5 metres per second.'''


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


def scoreboard(turn, altitude, velocity, fuel):
    """ Prints the scoreboard whenever it is called """
    sep = '-' * 50
    print('%s\nTurn: %d\nAltitude: %.1f metres' % (sep, turn, altitude))
    print('Velocity: %.1f m/s\nFuel: %.1f litres\n%s' % (velocity, fuel, sep))


def fuel_check(fuel):
    if fuel > 0:
        return float(input('How much fuel do you want to burn?: '))
    else:
        print('You\'re out of fuel')
        return 0


def burn_calc(fuel):
    print('-' * 50)
    burn = fuel_check(fuel)
    if burn < 0:
        return 0
    elif burn > fuel:
        return fuel
    else:
        return burn


def calc(fun, fuel, gravity, velocity):
    pass

#         fuel -= burn
#         velocity += gravity
#         velocity -= constant * burn
#         altitude -= velocity
#         turn += 1

# new_game = ready_player_one()
#
# while new_game:
#     turn = 0
#     altitude = 500.0
#     velocity = 0.0
#     fuel = 500.0
#     gravity = 2.0
#     constant = 0.15
#     while altitude > 0:
#         scoreboard()
#
#         if fuel <= 0:
#             print('------------------------------------------------')
#             print('Whoops you\'re out of fuel')
#             burn = 0
#         else:
#             print('------------------------------------------------')
#             burn = float(input('How much fuel do you want to burn?: '))
#
#         if burn < 0:
#             burn = 0
#         if burn > fuel:
#             burn = fuel
#
#         fuel -= burn
#         velocity += gravity
#         velocity -= constant * burn
#         altitude -= velocity
#         turn += 1
#
#     if velocity > 10.0:
#         print('------------------------------------------------')
#         print('You\'ve crashed. Creating a two mile crater.')
#     elif 10.0 >= velocity > 5.0:
#         print('------------------------------------------------')
#         print('You\'ve landed hard! You\'re final score is:')
#         altitude = 0.0
#         scoreboard()
#     else:
#         print('------------------------------------------------')
#         print('You\'ve landed safely! You\'re final score is:')
#         altitude = 0.0
#         scoreboard()
#
#     print('------------------------------------------------')
#     print('                       GAME OVER')
#     print('------------------------------------------------')
#


def main():
    turn = 0
    altitude = 500.0
    velocity = 0.0
    fuel = 500.0
    gravity = 2.0
    constant = 0.15
    instructions()
    scoreboard(turn, altitude, velocity, fuel)
    playing = True
    while playing:
        scoreboard(turn, altitude, velocity, fuel)
        while altitude > 0:
            burn = burn_calc(fuel)
            fuel -= burn
            velocity += gravity
            velocity -= constant * burn
            altitude -= velocity
            turn += 1
            scoreboard(turn, altitude, velocity, fuel)
    playing = play_again(input('Would you like to play again? (y/n): '))


if __name__ == '__main__':
    main()
