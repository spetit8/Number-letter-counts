#! Python 3

# This code will find the largest prime factor of a given number

print('Please input the number you would like the largest prime factor of')
Number = int(input())

for n in range(Number):
    if Number % n == 0 and n != Number:
        MaxPrime = n

print(MaxPrime)
