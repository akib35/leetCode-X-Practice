import bisect


class ExamTracker:
    def __init__(self):
        self.times = []
        self.scores = {}

    def record(self, time: int, score: int) -> None:
        if time in self.scores:
            self.scores[time] += score
        else:
            bisect.insort(self.times, time)  # Keep times sorted
            self.scores[time] = score

    def totalScore(self, startTime: int, endTime: int) -> int:
        lo = bisect.bisect_left(self.times, startTime)
        hi = bisect.bisect_right(self.times, endTime)
        total = 0
        for i in range(lo, hi):
            time = self.times[i]
            total += self.scores[time]
        return total


if __name__ == "__main__":
    s = ExamTracker()
    s.record(1, 98)
    print(s.totalScore(1, 1))  # 98
    s.record(5, 99)
    print(s.totalScore(1, 3))  # 98
    print(s.totalScore(1, 5))  # 197
    print(s.totalScore(3, 4))  # 0
    print(s.totalScore(2, 5))  # 99
