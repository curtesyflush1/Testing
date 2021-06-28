def find_the_evens(a,b):
    if a %2 ==0 and b %2 == 0:
        return (min(a,b))
    else:
        print (max(a,b))
find_the_evens(2,3)

# LESSER OF TWO EVENS: Write a function that returns the lesser of 
# two given numbers if both numbers are even, 
# but returns the greater if one or both numbers are odd