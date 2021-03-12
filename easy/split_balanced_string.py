from typing import List

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        out = 0
        curr_str = ""
        for i in range(len(s)):
            curr_str = curr_str + s[i]
            print(f"{i} : {curr_str}")
            if (curr_str.count("R") == curr_str.count("L")):
                out += 1
                curr_str = ""
        print(out)
        return out

if __name__ == '__main__':
    
    test1 = Solution()
    test1.balancedStringSplit("RLRRLLRLRL")
    test1.balancedStringSplit("RLLLLRRRLR")