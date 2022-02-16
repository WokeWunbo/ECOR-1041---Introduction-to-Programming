# Arun Karki 101219923

# Function Exercise 1
def first_last(list_int : list[int], x : int) -> bool:
    """Return True if the first or last element are 
    equal to an certain number
    
    >>> first_last([2,3,4,6], 2)
    True
    >>> first_last([1,5,2,6], 6)
    True
    >>> first_last([6,4,8,6]
    True
    >>> first_last([6,4,8,34], 2)
    False
    >>> first_last([3,2,2,1], 2)
    False
    """
    if len(list_int) <= 0:
        return False
    return (list_int[0] == x) or (list_int[len(list_int)-1] == x)

# Function Exercise 2
def common_end(list_int_one : list[int], list_int_two : list[int]) -> bool:
    """Return True if the first or last elements are 
    equal to first or last element of another list
    
    >>> common_end([2,3,4,6], [1,5,2,6])
    True
    >>> common_end([6,4,8,6], [6,4,8,34])
    True
    >>> common_end([1,4,8,3], [2,4,8,5])
    False
    """
    if len(list_int_one) <= 0 or len(list_int_two) <= 0:
        return False    
    return (list_int_one[0] == list_int_two[0]) or (list_int_one[len(list_int_one)-1] == list_int_two[len(list_int_two)-1]) or (list_int_one[0] == list_int_two[len(list_int_two)-1])

# Function Exercise 3
def average(lst_int : list[int]) -> float:
    """Returns the average of 5 elements in a given list
    
    >>> average([1,2,3,4,5])
    3.0
    >>> average([2,4,7,8,10])
    6.2
    >>> average([-2,4,7,-6,10])
    2.6
    """
    return (lst_int[0] + lst_int[1] + lst_int[2] + lst_int[3] + lst_int[4]) / len(lst_int)

# Function Exercise 4
def reverse(lst_int : list[int]) -> list[int]:
    """Returns a reversed table of given table
    
    >>> reverse([1, 2, 3, 4, 5])
    [5, 4, 3, 2, 1]
    >>> reverse([2, 4, 6, 8, 10])
    [10, 8, 6, 4, 2]
    >>> reverse([1, 4, 8, 3, 5])
    [5, 3, 8, 4, 1]
    """
    first = lst_int[0]
    second = lst_int[1]
    third = lst_int[2]
    fourth = lst_int[3]
    fifth = lst_int[4]
    return [fifth, fourth, third, second, first]

# Function Exercise 5
def max_list(list_int : list[int]) -> list[int]:
    """Returns table with all maximum values given a list 
    
    >>> max_list([1,2,3])
    [3, 3, 3]
    >>> max_list([2, 9, 3])
    [9, 9, 9]
    >>> max_list([12, 9, 9])
    [12, 12, 12]
    """
    max_int = max(list_int)
    return [max_int, max_int, max_int]

# Function Exercise 6
def middle_way(list_int_one : list[int], list_int_two : list[int]) -> list[int]:
    """Return the middle elements of given lists
    
    >>> middle_way([1, 2, 3], [4, 5, 6])
    [2, 5]
    >>> middle_way([4, 5, 3], [1, 2, 5])
    [5, 2]
    >>> middle_way([3, 94, 11], [23, 69, 59])
    [94, 69]
    """
    return [list_int_one[1], list_int_two[1]]

# Function Exercise 7
def has_elements(list_int : list[int], x : int, y : int) -> bool:
    """Function returns true if an element, or multiple elements, are present in a given list
    
    >>> has_elements([1,2,3,4,5], 10, 2)
    True
    >>> has_elements([1,2,3,4,5], 10, 20)
    False
    >>> has_elements([1,2,3,4,5], 1, 2)
    True
    >>> has_elements([1,2,3,4,5], -1 , 5)
    True
    """
    return x in list_int or y in list_int

# Exercise 1
print(first_last([3,2,2,1], 2))

# Exercise 2
print(common_end([2,3,4,6], [1,5,2,6]))

# Exercise 3
print(average([-2,4,7,-6,10]))

# Exercise 4
print(reverse([1, 2, 3, 4, 5]))

# Exercise 5
print(max_list([12, 9, 9]))

# Exercise 6
print(middle_way([1, 2, 3], [4, 5, 6]))

# Exercise 7
print(has_elements([1,2,3,4,5], 10, 2))