class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = s.lower()replace(" ", "")
        s = "".join(char.lower() for char in s if char.isalnum())

        print(s,s[::-1])
        for i,j in zip(s,s[::-1]):
            if i!=j:
                print(i,j)
                return False
        return True
        