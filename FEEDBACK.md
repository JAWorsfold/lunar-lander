CLONED

Good commit history.

Try and avoid
```
  """Asks if the player wants to play again."""
    if prompt == 'y' or prompt == 'Y':
        return True
    elif prompt == 'n' or prompt == 'N':
        print('Thanks for playing!')
        return False
    else:
        return play_again(input('Invalid entry. Try again (y/n): '))

```
prefer sets for validation and try to avoid returning `True`/`False`.

Use appropriate conventions for representing `CONSTANTS`,
```
    velocity = 0.0
    fuel = 500.0
    gravity = 2.0
    constant = 0.15
```

Maybe not the most transparent code
```
    """Takes the list of initial variables and calculates the new list."""
    vars = list
    burn = burn_calc(vars[3])
    vars[3] -= burn  # fuel after subtracting burn
    vars[2] += vars[4]  # velocity after adding gravity
    vars[2] -= vars[5] * burn  # veolcity after adding burn * constant
    vars[1] -= vars[2]  # altitude after subtracting velocity
    vars[0] += 1  # turn counter
    return vars


```
Normally the following applies, *Simple problem = simple code *

Good attempt.

Grade: A
