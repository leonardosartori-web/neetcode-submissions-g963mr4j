"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = deque()
        for interval in intervals:
            time.append((interval.start, 1))
            time.append((interval.end, -1))

        time = list(time)
        
        time.sort(key=lambda t: (t[0], t[1]))

        res = cnt = 0
        for t in time:
            cnt += t[1]
            res = max(res, cnt)
        return res