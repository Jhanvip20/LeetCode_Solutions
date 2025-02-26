class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set() #To store unique char in the window
        left = 0
        max_length = 0

        for right in range(len(s)):
            # If the character is already in the window, shrink the window from the left
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1 #Move the left pointer to the right to remove duplicate
            
            char_set.add(s[right])  #Add the current character to the set

            max_length = max(max_length, right - left + 1) #Update max_length of the window
        return max_length
        