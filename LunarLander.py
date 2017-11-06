'''Joseph Worsfold - jworsf01.
   This is the Lunar Lander (1.0) game which has been developed to be played
   multiple times within specific parameters. These parameters include the
   following: altitude, velocity, fuel, gravity, constant, burn. Each turn
   the player is asked how much fuel to burn, which will affect the downward
   velocity created by gravity, and this will affect the altitude on the next
   turn. Winners must get to zero or less altitude at a velociy under 10 metres
   per second. Extra points if it's under 5 metres per second.'''


def ready_player_one(ready=input('Are you ready to play a new game? (y/n): ')):
    """ Asks if the player is ready to initiate the game """
    if ready == 'y' or ready == 'Y':
        return True
    elif ready == 'n' or ready == 'N':
        print('Thanks for playing.')
        return False
    else:
        print('Invalid entry')
        again = ready_player_one(input('Try again (y/n): '))
        return again


def scoreboard():
    """ Prints the scoreboard whenever it is called """
    print('------------------------------------------------')
    print('Turn: ' + str(turn))
    print('Altitude: ' + str(round(altitude, 1)) + ' metres')
    print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
    print('Fuel: ' + str(round(fuel, 1)) + ' litres')


new_game = ready_player_one()

while new_game:
    turn = 0
    altitude = 500.0
    velocity = 0.0
    fuel = 500.0
    gravity = 2.0
    constant = 0.15
    while altitude > 0:
        scoreboard()
        if fuel <= 0:
            print('------------------------------------------------')
            print('Whoops you\'re out of fuel')
            burn = 0
        else:
            print('------------------------------------------------')
            burn = float(input('How much fuel do you want to burn?: '))

        if burn < 0:
            burn = 0
        if burn > fuel:
            burn = fuel

        fuel -= burn
        velocity += gravity
        velocity -= constant * burn
        altitude -= velocity
        turn += 1

    if velocity > 10.0:
        print('------------------------------------------------')
        print('You\'ve crashed. Creating a two mile crater.')
    elif 10.0 >= velocity > 5.0:
        print('------------------------------------------------')
        print('You\'ve landed hard! You\'re final score is:')
        altitude = 0.0
        scoreboard()
    else:
        print('------------------------------------------------')
        print('You\'ve landed safely! You\'re final score is:')
        altitude = 0.0
        scoreboard()

    print('------------------------------------------------')
    print('                       GAME OVER')
    print('------------------------------------------------')

    new_game = ready_player_one(input('Would you like to play again? (y/n): '))
