class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Keep only alphanumeric characters and convert to lowercase
        filtered_str = [char.lower() for char in s if char.isalnum()]
        
        # Check if the list equals its reverse
        return filtered_str == filtered_str[::-1]