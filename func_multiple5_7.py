import pytest
def multi(x):

    if x % 5 == 0 and x % 7 == 0:
        return("fizzbuzz")
    elif x % 7 == 0:
        return("buzz")
    elif x % 5 == 0:
        return("fizz")
    else:
        return("miss")
