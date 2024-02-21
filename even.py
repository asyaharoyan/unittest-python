def even_numbers_of_even(numbers):
    """
    Returning even numbers
    """
    if isinstance(numbers, list):
        evens = sum([1 for n in numbers if n % 2 == 0])

        return True if evens and evens % 2 == 0 else False

    else:
        raise TypeError("A list was not passed into the funktion.")

if __name__ == '__main__':
    even_numbers_of_even([2, 1, 4])