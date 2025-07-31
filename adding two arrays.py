nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# output [1,2,2,3,5,6]
def merge( nums1, m, nums2, n):
        a = []
        a = nums1 + nums2
        b = []
        for i in a:
                if i != 0:
                        b.append(i)
        
        b.sort()
        nums1 = b
        return nums1       
        
        
        
        




print(merge(nums1, m, nums2, n))