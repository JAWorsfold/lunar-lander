'''Joseph Worsfold - jworsf01.
   This is the Lunar Lander (1.0) game which has been developed to be played
   multiple times within specific parameters. These parameters include the
   following: altitude, velocity, fuel, gravity, constant, burn. Each turn
   the player is asked how much fuel to burn, which will affect the downward
   velocity created by gravity, and this will affect the altitude on the next
   turn. Winners must get to zero or less altitude at a velociy under 10 metres
   per second. Extra points if it's under 5 metres per second.'''

new_game = True

while new_game:
    ready_player = input('Are you ready to play (again)? (Y/N): ')
    altitude = 500.0
    velocity = 0.0
    fuel = 500.0
    turn = 0
    gravity = 2.0
    constant = 0.15
    if ready_player == 'Y' or ready_player == 'y':
        while altitude > 0:
            print('------------------------------------------------')
            print('Turn: ' + str(turn))
            print('Altitude: ' + str(round(altitude, 1)) + ' metres')
            print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
            print('Fuel: ' + str(round(fuel, 1)) + ' litres')
            print('------------------------------------------------')

            if fuel <= 0:
                print('Whoops you\'re out of fuel')
                burn = 0
            else:
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

        print('------------------------------------------------')
        print('Turn: ' + str(turn))
        print('Altitude: ' + str(round(altitude, 1)) + ' metres')
        print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
        print('Fuel: ' + str(round(fuel, 1)) + ' litres')
        print('------------------------------------------------')

        if velocity > 10.0:
            print('You\'ve crashed. Creating a two mile crater.')
        elif 10.0 >= velocity > 5.0:
            print('You\'ve landed hard. Marooned on the moon.')
            print('------------------------------------------------')
            print('Turn: ' + str(turn))
            print('Altitude: ' + str(round(altitude, 1)) + ' metres')
            print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
            print('Fuel: ' + str(round(fuel, 1)) + ' litres')
        else:
            print('You\'ve landed safely')
            print('------------------------------------------------')
            altitude = 0.0
            print('Turn: ' + str(turn))
            print('Altitude: ' + str(round(altitude, 1)) + ' metres')
            print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
            print('Fuel: ' + str(round(fuel, 1)) + ' litres')
    
        print('------------------------------------------------')
        print('            GAME OVER')
        print('------------------------------------------------')

    elif ready_player == 'N' or ready_player == 'n':
        print('Thanks for playing.')
        new_game = False
    else:
        print('Try again...')


