"""
input two of the three side in right angled triangle and return the third. use "?" to indicate the unknown side. 
"""

def pythagoras(opposite,adjacent,hypotenuse):
    if isinstance(opposite, str) and opposite == "?":
        return ("Opposite = " + str(((hypotenuse**2) - (adjacent**2))**0.5))
    elif isinstance(adjacent, str) and adjacent == "?":
        return ("Adjacent = " + str(((hypotenuse**2) - (opposite**2))**0.5))
    elif isinstance(hypotenuse, str) and hypotenuse == "?":
        return ("Hypotenuse = " + str(((opposite**2) + (adjacent**2))**0.5))
    else:
        raise ValueError("invalid argument were given.")
