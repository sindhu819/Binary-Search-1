'''
Binary search infinite loop
'''
class solution:
    def infinite(self,nums,target):
        low=0
        high=low+1
        temp=nums[0]
        while temp<target:
            low=high
            high=2*high
            temp=nums[high]
        print(low,high)
        return self.helper(low,high,nums,target)
    def helper(self,low,high,nums,target):
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1
    
m=solution()
m.infinite([2,5,6,8,9,12,14,15,17], 12)

