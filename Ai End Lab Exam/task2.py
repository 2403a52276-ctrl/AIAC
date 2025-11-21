import unittest


def parse_numbers_from_file(filename):
    """
    Read messy comma-separated numbers from a file, clean them,
    ignore empty values and extra spaces, and return a list of integers.

    Parameters:
        filename (str): the path of the input text file.

    Returns:
        list[int]: a cleaned list of integers.
    """

    # Open and read file content
    with open(filename, "r") as f:
        content = f.read()

    # AI-assisted cleaning:
    # - split by commas
    # - strip spaces
    # - ignore blanks and non-numeric values
    cleaned_numbers = []
    for value in content.split(","):
        num = value.strip()
        if num.isdigit():  # ensures only valid numbers are used
            cleaned_numbers.append(int(num))

    return cleaned_numbers


def sum_numbers(numbers):
    """
    Return the sum of a list of integers.

    Parameters:
        numbers (list[int])

    Returns:
        int: sum of numbers
    """
    return sum(numbers)


# -------------------------------
# MAIN EXECUTION (RUN PROGRAM)
# -------------------------------
if __name__ == "__main__":
    try:
        nums = parse_numbers_from_file("data.txt")  # file must exist
        total = sum_numbers(nums)

        print("Numbers found:", nums)
        print("Sum of numbers:", total)

    except FileNotFoundError:
        print("Error: data.txt file not found.")
        print("Create a file named data.txt in the same folder.")
        print("\nRunning Tests...\n")

    # -------------------------------
    # TEST CASES (unittest)
    # -------------------------------

    class TestParsing(unittest.TestCase):

        def test_clean_parsing(self):
            """Check parsing messy data."""
            data = "1, 2,3 ,4,,5"
            with open("temp.txt", "w") as f:
                f.write(data)

            result = parse_numbers_from_file("temp.txt")
            self.assertEqual(result, [1, 2, 3, 4, 5])

        def test_sum_function(self):
            """Check sum function."""
            self.assertEqual(sum_numbers([1, 2, 3]), 6)
            self.assertEqual(sum_numbers([]), 0)

        def test_ignore_invalid_values(self):
            """Ensure incorrect values are ignored."""
            data = "10, 20, , ,x, 30"
            with open("temp.txt", "w") as f:
                f.write(data)

            result = parse_numbers_from_file("temp.txt")
            self.assertEqual(result, [10, 20, 30])

    # Run all tests
    unittest.main(argv=[''], exit=False)
