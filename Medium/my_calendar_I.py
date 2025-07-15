class MyCalendar:

    def __init__(self):
        self.booked = []

    def book(self, startTime: int, endTime: int) -> bool:
        for bs, be in self.booked:
            if startTime < be and endTime > bs:
                return False

        self.booked.append((startTime, endTime))
        return True
