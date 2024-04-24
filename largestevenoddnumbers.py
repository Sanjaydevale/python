def largest_even_odd(lst):
    largest_even = None
    largest_odd = None

    for num in lst:
        if num % 2 == 0:
            if largest_even is None or num > largest_even:
                largest_even = num
        else:
            if largest_odd is None or num > largest_odd:
                largest_odd = num

    print("Largest even number:", largest_even if largest_even is not None else "None")
    print("Largest odd number:", largest_odd if largest_odd is not None else "None")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
largest_even_odd(numbers)
