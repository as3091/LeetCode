class Solution:
    def merge(self,left_arr,right_arr):
        merged = []
        for i in range(len(left_arr) + len(right_arr)):
            if len(left_arr) == 0:
                merged.append(right_arr.pop(0))
            elif len(right_arr) == 0:
                merged.append(left_arr.pop(0))
            elif left_arr[0] < right_arr[0]:
                merged.append(left_arr.pop(0))
            else:
                merged.append(right_arr.pop(0))
        return merged
    def mergeSort(self,arr):
        lenny = len(arr)
        if lenny > 1:
            mid = lenny // 2
            arr = self.merge(self.mergeSort(arr[:mid]), self.mergeSort(arr[mid:]))
        return arr
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr_3 = nums1+nums2
        arr_4 = self.mergeSort(arr_3)
        median = arr_4[len(arr_4) // 2] if len(arr_4) % 2 == 1 else (arr_4[len(arr_4) // 2 - 1] + arr_4[len(arr_4) // 2]) / 2
        return median