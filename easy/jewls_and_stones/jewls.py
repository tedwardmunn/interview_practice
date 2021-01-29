

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:

        lenJ = len(J)
        lenS = len(S)
        numOverlap = 0

        for x in range(lenJ):
            charJ = J[x]
            for y in range(lenS):
                charS = S[y]
                if charJ == charS:
                    numOverlap = numOverlap + 1

        return numOverlap

