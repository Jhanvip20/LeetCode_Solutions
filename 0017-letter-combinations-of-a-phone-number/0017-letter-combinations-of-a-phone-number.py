class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping of digits to letters as on a telephone keypad
        phone_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        # Base case: if the input string is empty, return an empty list
        if not digits:
            return []

        # List to hold the final combinations
        result = []

        # Backtracking function to generate combinations
        def backtrack(index, current_combination):
            # If the current combination is complete, add it to the result
            if index == len(digits):
                result.append(''.join(current_combination))
                return

            # Get the letters for the current digit
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                # Add the letter to the current combination
                current_combination.append(letter)
                # Recursively continue to the next digit
                backtrack(index + 1, current_combination)
                # Backtrack: remove the last letter and try the next one
                current_combination.pop()

        # Start the backtracking process from index 0 and an empty combination
        backtrack(0, [])

        return result