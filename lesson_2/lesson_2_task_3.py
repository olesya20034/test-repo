import math


def square(side):
    area = side * side
    if type(side) != int:
        return math.ceil(area)
    return area
print(square(4))    
print(square(2.5))  
print(square(3.0))