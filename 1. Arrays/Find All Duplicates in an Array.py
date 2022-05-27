class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        double = []
        
        for element in nums:
            index = abs(element)
            
            if nums[index-1]<0:
                double.append(index)
            else:
                nums[index-1] = -1*(nums[index-1])
        return double
        