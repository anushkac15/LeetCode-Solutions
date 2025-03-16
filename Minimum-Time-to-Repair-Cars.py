class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        l = 0
        r = max(ranks) * cars * cars

        def canRepairCarsInTime(mid: int) -> bool:
            total_cars = 0
            for rank in ranks:
                total_cars += int(sqrt(mid // rank))
            return total_cars >= cars

        while l < r:
            mid = (l + r) // 2
            if canRepairCarsInTime(mid):
                r = mid  
            else:
                l = mid + 1  

        return l
