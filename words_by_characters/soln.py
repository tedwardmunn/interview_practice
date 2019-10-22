

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        for x in range(len(words)):
            curr = words[x]
            # print(curr)
            checkCount = 0
            for z in range(len(curr)):
                charCurr = curr[z]
                # print(charCurr)
                for y in range(len(chars)):
                    charList = chars[y]
                    # print(charList)
                    if charCurr == charList:
                        checkCount = checkCount+1
            if checkCount >= len(curr):
                total = total + len(curr)
        return total
