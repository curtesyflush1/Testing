# Write a function that capitalizes the first and fourth letters 
# of a name.

def old_mcdonald(name):
    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()