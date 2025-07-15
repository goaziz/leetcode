class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for os, oe in self.overlaps:
            if startTime < oe and endTime > os:
                return False

        for bs, be in self.booked:
            if startTime < be and endTime > bs:
                overlap_start = max(startTime, bs)
                overlap_end = min(endTime, be)

                self.overlaps.append((overlap_start, overlap_end))

        self.booked.append((startTime, endTime))
        return True


myCalendarTwo = MyCalendarTwo()
myCalendarTwo.book(10, 20)
myCalendarTwo.book(50, 60)
myCalendarTwo.book(10, 40)
myCalendarTwo.book(5, 15)
myCalendarTwo.book(5, 10)
myCalendarTwo.book(25, 55)
