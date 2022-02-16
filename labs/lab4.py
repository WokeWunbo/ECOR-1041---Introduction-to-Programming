# Arun Karki 101219923
import math  

# Exercise 1 Function
def area_of_disk(radius): 
    return math.pi * radius ** 2  
def area_of_ring(outer, inner): 
    return area_of_disk(outer) - area_of_disk(inner) 

# Exercise 2 Function
LITERS_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_liters_per_100km(mpg): 
    return 100 * LITERS_PER_GALLON / KMS_PER_MILE / mpg

# Exercise 3 Function
def accumulated_amount(principal, rate, n, time):
    if n == 0:
        print("0 is not a valid input for n")
    else:
        return principal*((1+(rate/n))**(n*time))

# Exercise 4 Function
def area_of_cone(height, radius):
    return math.pi*(radius**2) + math.pi*radius*(math.sqrt((radius**2) + (height**2)))

# Main Script

# Exercise 1
area = area_of_disk(5) 
print(area)
area = area_of_disk(5.0) 
print(area)
area = area_of_ring(10, 5) 
print(area)
area = area_of_ring(10.0, 5.0)
print(area)

# Exercise 2
print("Exercise 2: 35 mpg =", convert_to_liters_per_100km(35), "1/100 km")
# print("Exercise 2: 35 mpg =", convert_to_liters_per_100km(35), "1/100 km")

# Exercise 3
print(accumulated_amount(1500, 0.043, 4, 6))

# Exercise 4
print(area_of_cone(5, 10)) 
# radius = 10, height = 5, outputs 665.4 as the area
# radius = 3, height = 4, outputs 75.4 as the area
# radius = 7, height = 8, outputs 387.71 as the area