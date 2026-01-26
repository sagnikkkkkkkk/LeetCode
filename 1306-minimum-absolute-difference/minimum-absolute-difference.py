class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        d = 10**8
        for i in range(1 , len(arr)):
            d = min(d , arr[i] - arr[i - 1])
        r = []
        for i in range(1 , len(arr)):
            if arr[i] - arr[i - 1] == d:
                r.append([arr[i - 1] , arr[i]])
        return r