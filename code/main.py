import numpy

def calculate_circle_area(radius):
    return numpy.pi * radius**2

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(numpy.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
