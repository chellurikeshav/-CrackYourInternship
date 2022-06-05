class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for i in range(len(nums1)):
            x = nums1[i]
            
            n2 = len(nums2)
            k = nums2.index(x)
            
            if k == n2-1:
                res.append(-1)
                continue
            
            found = False
            for j in range(k+1,n2):
                if nums2[j] > x:
                    res.append(nums2[j])
                    found = True
                    break
            
            if found == False:
                res.append(-1)
        return res
        