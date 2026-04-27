class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        arr.append(-1)
        for i in range(n-1, -1, -1):
            arr[i] = max(arr[i], arr[i+1])
        arr.pop(0)
        return arr