class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniques = set(nums)
        if len(uniques) != len(nums):
            return True
        return False
