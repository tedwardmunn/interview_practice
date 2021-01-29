from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = []
        for i in range(len(groupSizes)):
            if groupSizes[i] == 0:
                continue
            current = groupSizes[i]
            if current == 1:
                groups.append([i])
            temp_group = []
            temp_group.append(i)
            for j in range(i+1, len(groupSizes)):
                if groupSizes[j] == 0:
                    continue
                if groupSizes[j] == current:
                    temp_group.append(j)
                    groupSizes[j] = 0
                    if len(temp_group) == current:
                        groups.append(temp_group)
                        break
        print(groups)
        return groups


if __name__ == '__main__':
    # https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
    test1 = Solution()
    # test1.groupThePeople([3,3,3,3,3,1,3])
    test1.groupThePeople([2,2,1,1,1,1,1])