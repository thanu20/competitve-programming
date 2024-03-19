from sortedcontainers import SortedList
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        s=SortedList()
        ans=0
        for num1,num2 in zip(nums1,nums2):
            ans+=s.bisect_right(num1-num2+diff)
            s.add(num1-num2)
        return ans
