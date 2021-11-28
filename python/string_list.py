from typing import List


class StringSet:

    def __init__(self, strings) -> None:
        self.strings = strings
        self.index_nums = {}
        self.index_strs = {}

        for i in range(0, len(self.strings)):
            self.index_nums[i] = self.strings[i]
            self.index_strs[self.strings[i]] = i

        print(self.index_nums)
        print(self.index_strs)

    # four functions
    # add
    # delete
    # check if exists
    # return a uniformly random sample

    def add(self, str_to_add):
        map_len = len(self.index_nums)
        self.index_nums[map_len + 1] = str_to_add
        self.index_strs[str_to_add] = map_len + 1

        print("added")
        print(self.index_nums)
        print(self.index_strs)

    def delete(self, str_to_delete):
        # swap end and delete index
        # pop end
        map_len = len(self.index_nums)
        delete_index = self.index_strs[str_to_delete]
        end_str = self.index_nums[map_len]

        # remove the str to delete
        self.index_nums.pop(map_len)
        self.index_strs.pop(str_to_delete)

        # change position of end str
        self.index_strs[end_str] = delete_index
        self.index_nums[delete_index] = end_str

        print("deleted")
        print(self.index_nums)
        print(self.index_strs

if __name__ == "__main__":
    test=StringSet(strings=['monday', 'tuesday', 'wednesday'])
