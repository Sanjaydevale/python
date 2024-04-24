def sum_numbers(lst):
    sum_negative = 0
    sum_even_positive = 0
    sum_odd_positive = 0

    for num in lst:
        if num < 0:
            sum_negative += num
        elif num % 2 == 0 and num > 0:
            sum_even_positive += num
        elif num % 2 != 0 and num > 0:
            sum_odd_positive += num

    print("Sum of negative numbers:", sum_negative)
    print("Sum of positive even numbers:", sum_even_positive)
    print("Sum of positive odd numbers:", sum_odd_positive)

# Example usage
numbers = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
sum_numbers(numbers)
