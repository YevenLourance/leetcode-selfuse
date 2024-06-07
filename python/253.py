class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # meeting room sorted all start and end
        start_list = sorted(i[0] for i in intervals)
        end_list = sorted(i[1] for i in intervals)
        end_idx = 0
        room = 0
        for i in range(len(intervals)):
            cur_time = start_list[i]
            if cur_time >= end_list[end_idx]:
                # two pointers
                # if ended one before a new start 
                # compare next end time with next start time
                end_idx = end_idx+1 
            else:
                # if not ended add a new room
                room = room+1
        return room