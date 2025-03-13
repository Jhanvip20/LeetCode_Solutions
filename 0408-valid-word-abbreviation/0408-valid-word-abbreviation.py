class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0  # word's index - Pointer to traverse the `word`
        j = 0  # abbr's index - Pointer to traverse the abbreviation

        # Iterate while both pointers are within bounds
        while i < len(word) and j < len(abbr):
            # Case 1: Characters match, move both pointers
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue # Skip further checks and move to the next character
            
            # Case 2: If `abbr[j]` is not a digit or is a leading '0' (invalid abbreviation)
            if not abbr[j].isdigit() or abbr[j] == '0':
                return False # Abbreviations cannot start with '0' or contain non-numeric invalid characters
            
            # Case 3: Convert the numeric abbreviation into an integer
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j]) # Build the number digit by digit
                j += 1 # Move to the next character
            # Move the `i` pointer forward by `num` positions
            i += num
        
        # Ensure both pointers reach the end of their respective strings
        return i == len(word) and j == len(abbr)