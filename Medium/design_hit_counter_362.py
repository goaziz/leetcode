class HitCounter:

    def __init__(self):
        self.seconds = []

    def hit(self, timestamp: int) -> None:
        self.seconds.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while len(self.seconds) > 0 and timestamp - self.seconds[0] >= 300:
            self.seconds.pop(0)

        return len(self.seconds)
