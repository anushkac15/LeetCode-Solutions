class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f2r = {}
        self.f2c = {}
        self.c2f = defaultdict(SortedSet)

        for i in range(len(foods)):
            self.f2r[foods[i]] = ratings[i]
            self.f2c[foods[i]] = cuisines[i]
            self.c2f[cuisines[i]].add((-ratings[i], foods[i]))

    def changeRating(self, food: str, new_r: int) -> None:
        c = self.f2c[food]
        old = (-self.f2r[food], food)
        self.c2f[c].remove(old)
        self.f2r[food] = new_r
        self.c2f[c].add((-new_r, food))

    def highestRated(self, c: str) -> str:
        return self.c2f[c][0][1]
