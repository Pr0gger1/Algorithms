import math

def pi(eps: float) -> float:
    sum_total = current_member = 4.0
    sign: int = -1
    
    divider: int = 3
    
    while abs(current_member) > eps:
        current_member = sign * (4.0 / divider)
        sum_total += current_member
        
        sign *= -1
        divider += 2
        
    return sum_total
    

def sin(x: float, eps: float) -> float:
    sum_total: float = 0
    current_member: float = x
    
    divider: float = 3
    
    while abs(current_member) > eps:
        sum_total += current_member
        
        current_member *= -(x ** 2) / (divider * (divider - 1))
        divider += 2
        
    return sum_total


def cos(x: float, eps: float) -> float:
    sum_total: float = 0
    current_member: float = 1
    
    divider: float = 0

    while abs(current_member) > eps:
        sum_total += current_member
        divider += 2
        current_member *= -(x ** 2) / (divider * (divider - 1))
        
    return sum_total


def exp(x: float, eps: float) -> float:
    sum_total: float = 1 + x
    current_member: float = x
    
    divider: int = 2
    
    while abs(current_member) > eps:
        current_member *= x / divider
        sum_total += current_member
        
        divider += 1
        
    return sum_total