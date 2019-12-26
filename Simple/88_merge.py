#题目描述：
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 说明:
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
#
# 示例:
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 输出: [1,2,2,3,5,6]
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        # 先复制元素
        nums1cp = nums1[:m]
        i, j = 0, 0
        k = 0
        while i < m or j < n:
            if i < m and j < n:
                if nums1cp[i] < nums2[j]:
                    nums1[k] = nums1cp[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1
            else:
                if i < m:
                    nums1[k] = nums1cp[i]
                    i += 1
                if j < n:
                    nums1[k] = nums2[j]
                    j += 1
            k += 1

    def merge2(self, nums1, m: int, nums2, n: int) -> None:
        if not nums2:
            return nums1
        i = m-1
        j = n-1
        k = len(nums1)-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        if i > 0:
            while i >= 0:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
        if j >= 0:
            while j >= 0:
                nums1[k] = nums2[j]
                j -= 1
                k -=1

