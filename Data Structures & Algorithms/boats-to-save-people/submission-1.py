class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        counter = 0

        people.sort()

        while l <= r:
            if l == r:
                counter += 1
                break
            if people[l] + people[r] <= limit:
                l += 1
            
            counter += 1
            r -= 1
        

        return counter