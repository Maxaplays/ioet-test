import math_operations

def test_factorial_default() -> None:
    factorial = math_operations.factorial(5)
    assert type(factorial) is int
def test_combination_without_repetition_default() -> None:
    combination = math_operations.combination_without_repetition(["Rene","Laura","Sam"])
    assert type(combination) is int