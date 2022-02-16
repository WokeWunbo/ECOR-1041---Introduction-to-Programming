# Arun Karki 101219923

# Function Exercise 1
def factorial(n: int) -> int:  
    """Return n! for positive values of n.  
  
    >>> factorial(1)  
    1  
    >>> factorial(2)  
    2  
    >>> factorial(3)  
    6  
    >>> factorial(4)  
    24  
    """      
    fact = 1      
    for i in range(2,n+1):  
        fact = fact * n  
     
    return fact

# Function Exercise 2
def triangle_type(angle_x : int, angle_y : int, angle_z : int) -> str:
    """The function returns the type of triangle based on given angles
    
    >>> triangle_type(60, 60, 60)
    Acute-Triangle
    >>> triangle_type(90, 60, 60)
    Right-Triangle
    >>> triangle_type(110, 10, 10)
    Obtuse-Triangle
    """
    sum_angles = angle_x + angle_y + angle_z
    if sum_angles > 180:
        print("Not a triangle.")
        return
    
    if (angle_x == 90) or (angle_y == 90) or (angle_z == 90):
        return "Right-Triangle"
    elif (angle_x > 90) or (angle_y > 90) or (angle_z > 90):
        return "Obtuse-Triangle"
    else:
        return "Acute-Triangle"
    
# Function Exercise 3
def discount(age : int, price : float) -> str:
    """The function returns the price in dollars after accounting
    for discount based on age
    
    >>> discount(24, 100)
    5.0$
    >>> discount(68, 100))
    16.0$
    >>> discount(256, 100)
    20.0$
    """
    discount = 0
    if 18 <= age < 40:
        discount = 5
    elif 40 <= age < 60:
        discount = 13
    elif 60 <= age < 80:
        discount = 16
    elif age >= 80:
        discount = 20
    return str((discount/100 * price)) + "$"

# Function Exercise 4
def test_int(test_number : int, actual : int, expected_value : int) -> int:
    """Returns 0 or 1 depending on if actual value equals the expected value
    
    >>> test_int(1, 1, 1)  
    1  
    >>> test_int(3, 6, 2)  
    1
    >>> test_int(3)  
    6  
    >>> test_int(4)  
    24  
    """
    print("Testing test_int (" + str(test_number) + ")")
    print("Expected result:", str(expected_value), "Actual result:", str(actual))
    if actual == expected_value:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0
    
# Main Script

# Exercise 1

# Count all fails/passes
total_pass = 0
total_fail = 0

# First
one_factorial = factorial(1) # = 1
print("Testing factorial(1)")
print("Expected result: 1 Actual result:", one_factorial)
if one_factorial == 1:
    total_pass+=1
    print("Test passed")
else:
    total_fail+=1
    print("Test failed")
    
# Second
two_factorial = factorial(2) # = 2
print("Testing factorial(2)")
print("Expected result: 2 Actual result:", two_factorial)
if two_factorial == 2:
    total_pass+=1
    print("Test passed")
else:
    total_fail+=1
    print("Test failed")

# Third
three_factorial = factorial(3) # = 6
print("Testing factorial(3)")
print("Expected result: 6 Actual result:", three_factorial)
if three_factorial == 6:
    total_pass+=1
    print("Test passed")
else:
    total_fail+=1
    print("Test failed")
    
# Four
four_factorial = factorial(4)  # = 24
print("Testing factorial(4)")
print("Expected result: 24 Actual result:", four_factorial)
if four_factorial == 24:
    total_pass+=1
    print("Test passed")
else:
    total_fail+=1
    print("Test failed")

# Five with revised code
if test_int(5, 120, factorial(5)) == 1:
    total_pass+=1
else:
    total_fail+=1
    
print(total_pass, "tests passed for Exercise 1")
print(total_fail, "tests failed for Exercise 1")

# Exercise 2
print(triangle_type(60, 60, 60))

# Exercise 3       
print(discount(256, 100))

# Exercise 4
test_int(1, 1, factorial(1))