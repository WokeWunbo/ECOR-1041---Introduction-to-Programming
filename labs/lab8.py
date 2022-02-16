# Arun Karki 101219923
 
# Function Exercise 1

BASE_PRICE = 30.00
WEEKEND_PRICE = 40.00
SENIOR_DISCOUNT = 50
YOUTH_DISCOUNT = 30

def ticket_price(age : int, weekday_weekend : bool) -> float:
    """Returns price after discount given the 
    weekday and discount applied
    
    >>> ticket_price(5, True)
    52.0
    >>> ticket_price(5, False)
    39.0
    >>> ticket_price(18, True)
    40.0
    >>> ticket_price(66, False)
    45.0
    """
    discount = 0
    if weekday_weekend: BASE_PRICE = WEEKEND_PRICE
    
    if age >= 65:
        discount = SENIOR_DISCOUNT
    elif age <= 12:
        discount = YOUTH_DISCOUNT
    
    return (BASE_PRICE * (discount/100)) + BASE_PRICE

# Function Exercise 2

def great_42(a : int, b : int) -> bool:
    """Returns if two values are equal to 42 or 
    if their sum/difference equals 42
    
    >>> great_42(2, 42)
    True
    >>> great_42(40, 2)
    True
    >>> great_42(2, 41)
    False
    """  
    return (a == 42) or (b == 42) or (abs(a-b) == 42) or (abs(a+b) == 42)

# Function Exercise 3

def sort_integers(int1 : int, int2 : int, int3 : int) -> str: 
    """Returns smallest to largest order of 3 given inputs
    
    >>> sort_integers(19, 11, 15)
    11, 15, 19
    >>> sort_integers(756, 14, 165)
    14, 165, 756
    >>> sort_integers(17, 32, 854)
    17, 32, 854
    """
    smallest = min(int1, int2, int3)
    between = 0
    largest = max(int1, int2, int3)
    
    if int1 > smallest and int1 < largest:
        between = int1
    elif int2 > smallest and int2 < largest:
        between = int2
    elif int3 > smallest and int3 < largest:
        between = int3
    
    return str(smallest) + ", " + str(between) + ", " + str(largest)

# Function Exercise 4

def gross_earnings(hours : int, wage : float) -> float:
    """Return earnings given wage and hours (overtime if accountable)
    
    >>> gross_earnings(70, 14.25)
    1211.25
    >>> gross_earnings(30, 14.25)
    427.5
    >>> gross_earnings(120, 14.25)
    2280.0
    """    
    return ((hours - (0 or (hours > 40) and (hours - 40))) * wage) + ((0 or (hours > 40) and (hours - 40)) * wage * 1.5)

# Function Exercise 5

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
    
def test_float(test_number : float, actual : float, expected_value : float) -> float:
    """Returns 0 or 1 depending on if actual value equals the expected value
    
    >>> test_float(1, 1, 1)  
    1  
    >>> test_float3, 6, 2)  
    1
    >>> test_float(3)  
    6  
    >>> test_float(4)  
    24  
    """
    print("Testing test_float (" + str(test_number) + ")")
    print("Expected result:", str(expected_value), "Actual result:", str(actual))
    if actual == expected_value:
        print("Test passed")
        return 1
    else:
        print("Test failed")
        return 0

# Main Script

# Exercise 1
print(ticket_price(5, True))

# Exercise 2
print(great_42(100, 58))

# Exercise 3
print(sort_integers(19, 11, 15))

# Exercise 4
print(gross_earnings(120, 14.25))