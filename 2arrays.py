# just things to check my commits

nums1 = [1,2,3,0,0,0] # length = 6 = n + m = 3 + 3
nums2 = [2,5,6] # length = n = 3

def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1



merge(nums1,3, nums2, 3)
print(nums1)
