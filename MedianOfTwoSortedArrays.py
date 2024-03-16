import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ptr1 = 0
        ptr2 = 0
        pos = 0
        x = 0
        y = 0
        l = len(nums1) + len(nums2)
        sd = True # True for single digit median, False for double digit median 
        result = [0 for i in range(l)]

        if nums1 == [] and nums2 == []:
            return []
        elif nums1 == []:
            return statistics.median(nums2)
        elif nums2 == []:
            return statistics.median(nums1)

        if l % 2 == 0:
            sd = False

        if sd:
            x = l/2
        else:
            x = l//2 - 1
            y = x+1

        while pos < l:
            if ptr1 == len(nums1):
                result[pos] = nums2[ptr2]
                ptr2 += 1
            elif ptr2 == len(nums2):
                result[pos] = nums1[ptr1]
                ptr1 += 1
            elif nums1[ptr1] < nums2[ptr2]:
                result[pos] = nums1[ptr1]
                ptr1 += 1
            else:
                result[pos] = nums2[ptr2]
                ptr2 += 1

            if sd:
                if pos == x:
                    return result[pos]
            elif not sd and pos == y:
                return (result[x]+result[y])/2
            pos += 1

        return statistics.median(result)
