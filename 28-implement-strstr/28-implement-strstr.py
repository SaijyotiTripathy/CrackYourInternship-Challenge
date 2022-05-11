class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:    #O(n)
            return haystack.index(needle)     #O(n)
        else:
            return -1