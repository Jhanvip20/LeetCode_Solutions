class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Count the frequency of each character in the string
        char_count = Counter(s)      # Count the number of characters that appear an odd number of times
        odd_count = sum(freq % 2 for freq in char_count.values())  # A string can be permuted into a palindrome if there is at most
        # one character that appears an odd number of times
        return odd_count <= 1