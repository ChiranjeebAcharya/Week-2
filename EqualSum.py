
class Solution:

    def equilibrium(self, arr):
        n = len(arr)
        total_sum = sum(arr)
        leftsum = 0
        for i, num in enumerate(arr):
            total_sum -= num

            if leftsum == total_sum:
                return "true"
            leftsum += num
        return "false"
