class MyCalendarTwo:

    def __init__(self):

        self.calendar = []
        self.overlap = []

    def book(self, start: int, end: int) -> bool:

        for x in self.overlap:

            if x[0] < end and x[1] > start:
                return False

        for x in self.calendar:

            if x[0] < end and x[1] > start:
                self.overlap.append([max(x[0], start), min(x[1], end)])

        self.calendar.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)
