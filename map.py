numbers = [10,20,30,40]


def square(number):
  return number * number


squared_numbers = map(square, numbers)


result = list(squared_numbers)
print(result) 