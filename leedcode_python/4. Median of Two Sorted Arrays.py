class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums3 = []
        nums3.extend(nums1)
        nums3.extend(nums2)
        nums3.sort()
        
        size = float(len(nums3))
        index = int(size / 2 )  #無條件捨去

        return float(nums3[index-1] + nums3[index])/2 if size % 2 == 0 else nums3[index]