class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ''
        str_list = []
        for i in range(len(s)):
            temp_char = s[i]
            # if temp char is in temp str
            repeat = False
            for j in range (len(temp_str)):
                if temp_char == temp_str[j]:
                    repeat = True

            str_list.append(temp_str)
            if repeat:
                temp_str = ''
            else:
                temp_str = temp_str + temp_char

        longest_count = 0
        longest_string = ''
        for i in range(len(str_list)):
            if len(str_list[i]) > longest_count:
                longest_count = len(str_list[i])
                longest_string = str_list[i]
        print(str_list)
        print(longest_string)
        print(longest_count)

if __name__ == '__main__':
    problem = Solution
    problem.lengthOfLongestSubstring('a', 'abcabcbb')
    problem.lengthOfLongestSubstring('a', 'bbbbbbbbbbbb')
    problem.lengthOfLongestSubstring('a', 'pwwkew')