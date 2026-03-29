class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        answer = []
        i = j = 0
        while (i < len(nums1) and j < len(nums2)):
            if nums1[i] == nums2[j] :
                if not answer or answer[-1] != nums1[i]: 
                    answer.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return answer