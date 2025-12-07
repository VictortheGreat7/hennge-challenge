def greater_lethal():
    import sys

    INT32_MAX = 2147483647
    INT32_MIN = -2147483648

    def sum_fourth_power_of_negatives(numbers, accumulated=0):
        if not numbers:
            return accumulated

        first, *remaining = numbers
        contribution = first ** 4 if first < 0 else 0
        accumulator = accumulated + contribution

        if accumulator > INT32_MAX or accumulator < INT32_MIN:
            return None

        return sum_fourth_power_of_negatives(remaining, accumulator)

    def convert_strings_to_integers(string_parts):
        if not string_parts:
            return []
        return [int(string_parts[0])] + convert_strings_to_integers(string_parts[1:])

    def read_exact_integer_count(expected_count):
        instruction = read_instruction()
        parts = instruction.split()
        if len(parts) != expected_count:
            return None
        return convert_strings_to_integers(parts)

    def process_test_cases(amount_left):
        if amount_left == 0:
            return []
        instruction = read_instruction()
        if instruction == '':
            return [-1] + process_test_cases(amount_left - 1)
        integer_count = int(instruction)
        numbers = read_exact_integer_count(integer_count)
        if numbers is None:
            return [-1] + process_test_cases(amount_left - 1)
        return [sum_fourth_power_of_negatives(numbers)] + process_test_cases(amount_left - 1)

    def read_instruction():
        instruction = sys.stdin.readline()
        if not instruction:
            return ''
        return instruction.strip()

    first_instruction = read_instruction()
    if first_instruction == '':
        return

    num_of_test_cases = int(first_instruction)
    test_case_results = process_test_cases(num_of_test_cases)

    sys.stdout.write("\n".join(map(str, test_case_results)))


if __name__ == "__main__":
    greater_lethal()