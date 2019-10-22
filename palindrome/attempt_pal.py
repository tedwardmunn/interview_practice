from string import ascii_lowercase

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()

        clean = lower
        lengthIn = len(lower)
        for x in range(lengthIn):
            y = lower[x]
            # we ignore grammar and consider letters/numbers
            # print(y)
            # print(y.isalpha())
            if y.isalpha() != True and y.isdigit() != True:
                clean = clean.replace(y,'')

        copy = clean
        print(clean)
        copy = clean[::-1]
        print(copy)
        if copy == clean:
            return 1
            print('true')
        else:
            return 0
            print('false')
