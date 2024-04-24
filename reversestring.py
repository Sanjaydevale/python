class StringReverser:
    def __init__(self, string):
        self.string = string
    
    def reverse(self):
        return self.string[::-1]


if __name__ == "__main__":
    input_string = input("Enter a string: ")
    reverser = StringReverser(input_string)
    reversed_string = reverser.reverse()
    print("Reversed string:", reversed_string)
