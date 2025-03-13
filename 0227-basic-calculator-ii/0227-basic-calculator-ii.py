class Solution:
    def calculate(self, s: str) -> int:
        stack = []  # Stack to store intermediate results
        num = 0  # Stores the current number
        sign = '+'  # Keeps track of the last operator
        s = s.replace(" ", "")  # Remove spaces for easier processing

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  # Build the full number

            if char in "+-*/" or i == len(s) - 1:  # Process when an operator is encountered or end of string
                if sign == '+':
                    stack.append(num)  # Push number to stack
                elif sign == '-':
                    stack.append(-num)  # Push negative number to stack
                elif sign == '*':
                    stack.append(stack.pop() * num)  # Perform multiplication
                elif sign == '/':
                    stack.append(int(stack.pop() / num))  # Perform integer division

                num = 0  # Reset current number
                sign = char  # Update operator

        return sum(stack)  # Sum up all values in the stack
