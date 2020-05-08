class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortedList = sorted(intervals)
        n = len(sortedList)
        previous_end = None

        for i in range(n):
            current_start, current_end = sortedList[i]
            if previous_end != None and (previous_end > current_end or previous_end > current_start):
                return False
            previous_end = current_end
            previous_start = current_start

        return True