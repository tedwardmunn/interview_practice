class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = s.replace(' ','')
        clean = clean.replace(',','')
        clean = clean.replace(':','')
        clean = clean.lower()
        copy = clean
        copy = clean[::-1]
        print(copy)
        if copy == clean:
            return 1
        else:
            return 0
