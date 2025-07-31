#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).


nums1 = [1,2]
nums2 = [3,4]

# --> 2 because [1,2,3]


def median(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    
    new_array = nums1 + nums2
    new_array.sort()

    if len(new_array) % 2 == 1:
        return new_array[len(new_array) // 2]
    else:
        return (new_array[len(new_array) // 2] + new_array[(len(new_array) - 1) // 2]) / 2


print(median(nums1,nums2))
