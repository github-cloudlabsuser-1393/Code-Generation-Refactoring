# Maximum number of elements allowed in the array
MAX_ELEMENTS = 100

def get_integer(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(prompt))
            if (min_value is not None and value < min_value) or (max_value is not None and value > max_value):
                print(f"Please enter a number between {min_value} and {max_value}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    try:
        n = get_integer(f"Enter the number of elements (1-{MAX_ELEMENTS}): ", 1, MAX_ELEMENTS)
        arr = []
        for _ in range(n):
            arr.append(get_integer("Enter an integer: "))
        total = sum(arr)
        print(f"Sum of the numbers: {total}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")

if __name__ == "__main__":
    main()
