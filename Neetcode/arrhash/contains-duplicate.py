#Coded by Aman Dhiraj

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictDuplicate = Counter(nums)
        for i in dictDuplicate:
            if i > 1:
                return true
        return false