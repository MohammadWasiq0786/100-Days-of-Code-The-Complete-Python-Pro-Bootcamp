"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1. Wikipedia  
You need to write a function called is_prime() that checks whether if the number passed into 
it is a prime number or not.  It should return True or False.

e.g.
7 is a primer number because it is only divisible by 1 and itself.
But 4 is not a prime number because you can divide it by 1, 2 or 4.
NOTE: 2 is a prime number because it's only divisible by 1 and itself, but 1 is not a prime number because it is only divisible by 1.

Example Input 1: 73; Example Output 1: True
Example Input 2: 75; Example Output 2: False
"""

def is_prime(n):
    # Check if n is less than 2
    if n < 2:
        return False
    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
print(is_prime(73))  
print(is_prime(75))  

#  ==================== OR ===================

def is_prime(num):
    if num == 2:
        return True
    if num == 1:
        return False
 
    # Loop through all the numbers between 2 and the number
    for i in range(2, num):
        # Check if the number (num) can be divided by the potential prime number
        if num % i == 0:
            return False
 
    # this return is outside the for loop which will only run once the loop finishes and none of the numbers are divisible. Therefore it is prime.
    return True