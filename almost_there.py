# ALMOST THERE: Given an integer n, return True if n is 
# within 10 of either 100 or 200

def almost_there(x):
    #num1 = range(90,110)
    if x in range(90,110,1):
        return True
    elif x in range(190,210,1):
        return True
    else:
        return False

# Or the following:

def almost_there(x):
    return (abs(100-x) <= 10) or (abs(200-x) <= 10)