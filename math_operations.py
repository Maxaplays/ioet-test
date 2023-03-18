def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def combination_without_repetition(names):
    return int(factorial(len(names))/(factorial(2)*(factorial(len(names)-2))))
    