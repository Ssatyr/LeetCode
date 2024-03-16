class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        maxlen = 0
        cmap = {}
        left = 0

        for right in range (l):
            if s[right] not in cmap or cmap[s[right]] < left:
                cmap[s[right]] = right
                maxlen = max(maxlen, right-left+1)
            else:
                left = cmap[s[right]] + 1
                cmap[s[right]] = right

        return maxlen
