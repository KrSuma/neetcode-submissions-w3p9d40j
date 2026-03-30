class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 1. Initialize pointers at the absolute boundaries
        l, r = 0, len(arr) - 1
        
        # 2. Keep shrinking as long as our window is larger than k
        # Note: 'r - l >= k' is the same as 'window_size > k'
        while r - l >= k:
            # 3. Compare the "pain" of the two outermost elements.
            # If the left distance is smaller or equal to the right distance, 
            # the right element is the "worse" candidate.
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1 # Discard the right element
            else:
                l += 1 # Discard the left element

        # 4. Return the finalized window
        return arr[l: r + 1]

        