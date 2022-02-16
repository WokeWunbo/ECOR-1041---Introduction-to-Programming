# Arun Karki 101219923

# Function Exercise 1
def Fibonacci_sequence(n : int) -> list[int]:
    """Returns a list of Fibonacci sequence 
    given a limit number
    
    >>> Fibonacci_sequence(6)
    [0, 1, 1, 2, 3, 5]
    >>> Fibonacci_sequence(13)
    [0, 1, 1, 2, 3, 5, 8, 13]
    >>> Fibonacci_sequence(13)
    [0, 1, 1, 2, 3, 5, 8, 13, 21]
    >>> Fibonacci_sequence(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    
    fib_numbers = []
    counter = 1
    start = 0
    next_number = 0
    
    while next_number <= n:
        fib_numbers += [next_number]
        start = counter
        counter = next_number
        next_number += start
    return fib_numbers

# Function Exercise 2
def max_min() -> str:
    """Returns a list and its max and min elements after looping
    
    >>> max_min()
    Please enter an integer (enter zero to quit): <user types <3>> 
    Please enter an integer (enter zero to quit): <user types <10>> 
    Please enter an integer (enter zero to quit): <user types <0>>
    The list = [10, 3], max = 10, min = 0
    """
    
    max_number, min_number = 0, 0
    question = "Please enter an integer (enter zero to quit): "
    integers_stored = []
    flag = True 
    
    while flag:
        user_input = int(input(question))
        if user_input == 0:
            flag = False
        else:
            integers_stored += [user_input]
            
    for x in range(0, len(integers_stored)):
        if integers_stored[x] > integers_stored[x-1]:
            max_number = integers_stored[x]
        elif integers_stored[x] < integers_stored[x-1]:
            min_number = integers_stored[x]
    
    return "The list = " + str(integers_stored) + ", max = " + str(max_number) + ", min = " + str(min_number)

# Function Exercise 3
def max_occurrences(list_integers : list[int]):
    """Returns the most occuring number in a list
    
    >>> max_occurrences([1,2,2,0])
    The most occuring number was 1
    >>> max_occurrences([1,1,1,2,2,0])
    The most occuring number was 2
    >>> max_occurrences([5,3,0,4,4])
    The most occuring number was 4
    """
    
    max_found = 0
    the_number = 0
    for number in list_integers:
        counter = 0
        for x in list_integers:
            if number == x:
                counter += 1
        if counter >= max_found:
            max_found = counter
            the_number = number
    return the_number

# Function Exercise 4
def bank_statement(account_balance : float, transactions : list[float]) -> float:
    """Returns new balance after transaction history calculated
    
    >>> bank_statement(50, [-200,100,300])
    250.0
    >>> bank_statement(34.33, [-1.53,23,2.55])
    58.35
    >>> bank_statement(134.33, [-11.53,123,12.55])
    258.35
    """
    # transcations = [-200,100,300], returns
    total = 0
    for amount in transactions:
        total += amount
    return round(float(total + account_balance), 2)

# Function Exercise 5
def prime_numbers(lower : int, upper : int):
    """Returns all prime number within an upper and lower bound
    
    >>> prime_numbers(1, 4)
    [1, 2, 3]
    >>> prime_numbers(1, 50)
    [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    >>> prime_numbers(5, 25)
    [5, 7, 11, 13, 17, 19, 23]
    >>> prime_numbers(35, 5)
    [5, 7, 11, 13, 17, 19, 23, 29, 31]
    """
    
    prime_numbers = []
    if lower >= upper:
        temporary = upper
        upper = lower
        lower = temporary     
    for number in range(lower, upper):
        is_prime = True
        for x in range(2, number):
            if number % x == 0:
                is_prime = False
        if is_prime: prime_numbers += [number]
    print(prime_numbers)
    
# Main Script

# Exercise 1
print(Fibonacci_sequence(6))

# Exercise 2
print(max_min())

# Exercise 3
print("The most occuring number was", max_occurrences([1,1,1,2,2,0]))

# Exercise 4
print(bank_statement(50, [-200,100,300]))

# Exercise 5
prime_numbers(35, 5)