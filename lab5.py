# Arun Karki 101219923

# Import math library
import math

# Exercise 1 Function
def volume_spherical_segment(height : int, baseRadius : int, topRadius : int) -> float:
    """
    Return volume of a spherical segment given the height,
    and radii of top and bottom circles
    
    >>> volume_spherical_segment(1,2,4)
    31.93952531149623
    >>> volume_spherical_segment(2,3,4)
    82.72860654453122
    """
    return (1/6)*math.pi*height*((3*(baseRadius**2)) + (3*(topRadius**2)) + (height**2))

# Exercise 2 Function
def equivalent_interest_rate(R : float, m : int, q : int) -> float:
    """
    Return the Equivalent Interest Rate percent in decimal form given,
    the Interest Rate (R), Compounding months (m), New Compounding (q)
    
    >>> equivalent_interest_rate(4,12,4)
    0.040133481481482214
    >>> equivalent_interest_rate(8, 12, 5)
    0.08037366485403874
    """   
    r = R/100
    interest = q*(((1+(r/m))**(m/q))-1)*100
    if interest < 0:
        print("Equivalent Interest Rate is negative.")
    else:
        return interest

# Main Script

# Exercise 1
print(volume_spherical_segment(1,2,4))

# Exercise 2
print(equivalent_interest_rate(4,12,4), "%")