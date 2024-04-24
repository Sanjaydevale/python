def is_neon_number(num):
    square = num ** 2
    digit_sum = 0
    while square > 0:
        digit_sum += square % 10
        square //= 10
    return digit_sum == num

def main():
    num = int(input("Enter a number to check if it's a neon number: "))
    if is_neon_number(num):
        print(num, "is a neon number.")
    else:
        print(num, "is not a neon number.")

if __name__ == "__main__":
    main()
