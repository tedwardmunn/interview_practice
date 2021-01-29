from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output = [first]
        for i in range(len(encoded)):
            output.append(output[i] ^ encoded[i])
        return output

if __name__ == '__main__':
    # https://leetcode.com/problems/decode-xored-array/
    test1 = Solution()
    print(test1.decode(encoded = [1,2,3], first = 1))