'''Joseph Worsfold - jworsf01.
   Then your description of what the program does.'''

# The game is not timed: 1 turn = 1 second
# Keep track of the number of turns/seconds to land
# Variables are Altitude/Velocity/Fuel
# Values to start 1000.0/0.0/1000.0

# User specify how much fuel to burn each turn
# Zero is legal - if asked more burn all - negative = 0

# Game ends when your altitude becomes zero or less
# A safe landing occurs if your speed is under 10m/s

# Each turn velocity increases by 1.6 metres/seconds
# Decreases by proportional amount to fuel burn by some constant - start with 0.15
# Altitude decreases by your velocity multiplied by amount of time...
# fuel decreases by the amount you burn, or total if requesting more

# Determine if you have landed
# Altitude is zero or less
# If successful print altitude of zero and final numbers
# if crash, use velocity to print out how deep a crater you have mde is
# after each game ask if the user wants to play again

altitude = 1000.0
velocity = 0.0
fuel = 1000.0
turn = 0
gravity = 1.6
constant = 0.15

while altitude > 0:
    print('----------------')
    print('Turn: ' + str(turn))
    print('Altitude: ' + str(round(altitude, 1)) + ' metres')
    print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
    print('Fuel: ' + str(round(fuel, 1)) + ' litres')
    print('----------------')

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
    
print('----------------')
print('Landed or Crashed...')
print('----------------')
print('Turn: ' + str(turn))
print('Altitude: ' + str(round(altitude, 1)) + ' metres')
print('Velocity: ' + str(round(velocity, 1)) + ' metres/second')
print('Fuel: ' + str(round(fuel, 1)) + ' litres')
print('----------------')


