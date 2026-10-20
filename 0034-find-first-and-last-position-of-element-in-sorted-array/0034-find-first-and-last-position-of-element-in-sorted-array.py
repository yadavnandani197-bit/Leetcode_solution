class Solution(object):
    def searchRange(self, nums, target):
        def findFirst():
            l, r = 0, len(nums)-1
            ans = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    ans = mid
                    r = mid - 1  # go left for first
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

        def findLast():
            l, r = 0, len(nums)-1
            ans = -1
            while l <= r:
                mid = (l+r)//2
                if nums[mid] == target:
                    ans = mid
                    l = mid + 1  # go right for last
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
        
        return [findFirst(), findLast()]
        
        

            
        