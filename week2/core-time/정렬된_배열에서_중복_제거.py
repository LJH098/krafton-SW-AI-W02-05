class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        memory = 0
        for i in range(len(nums)):
            if i == 0:
                memory = nums[i]

            elif memory == nums[i]:
                nums[i] = "_"
            else:
                memory = nums[i]
        new_idx = 0

        for i in range(len(nums)):
            if nums[i] != "_":
                nums[i], nums[new_idx] = nums[new_idx], nums[i]
                new_idx += 1
        print(nums)
        return new_idx
