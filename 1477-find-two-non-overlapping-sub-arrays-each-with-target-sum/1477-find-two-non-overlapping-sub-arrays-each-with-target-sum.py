class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        prefix_sum = {0: -1}
        curr_sum = 0
        dp = [float('inf')] * n
        min_len = float('inf')
        ans = float('inf')
        
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum - target in prefix_sum:
                prev_idx = prefix_sum[curr_sum - target]
                subarray_len = i - prev_idx
                if prev_idx >= 0:
                    ans = min(ans, dp[prev_idx] + subarray_len)
                min_len = min(min_len, subarray_len)
            dp[i] = min_len
            prefix_sum[curr_sum] = i
        
        return ans if ans != float('inf') else -1
        