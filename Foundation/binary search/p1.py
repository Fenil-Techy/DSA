class Solution():
    def first_occurrence(self,arr, target):
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                high = mid - 1   # keep searching LEFT
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return result

    def last_occurrence(self,arr, target):
        low, high = 0, len(arr) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                result = mid
                low = mid + 1   # keep searching RIGHT
            elif target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return result

    def search_range(self,arr, target):
        return (self.first_occurrence(arr, target), self.last_occurrence(arr, target))

    
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
s=Solution()
print(s.search_range(arr, target))  # Output: (1, 3)

