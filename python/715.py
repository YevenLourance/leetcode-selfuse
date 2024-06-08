class RangeModule:

#inspired by a genius
    def __init__(self):
        self.track = []
        # tracking array of integers
        # consists of a number of sorted pairs of start and end values
        # always has an even number of elements

    def addRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        subtrack = []
        if start % 2 == 0:
            # outside the range of start and end indexes being tracked
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        self.track[start:end] = subtrack
        

    def removeRange(self, left, right):
        start = bisect.bisect_left(self.track, left)
        end = bisect.bisect_right(self.track, right)
        
        subtrack = []
        if start % 2 == 1:
            # ins ide the range of start and end indexes being tracked
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
			
        self.track[start:end] = subtrack
		
    def queryRange(self, left, right):
        start = bisect.bisect_right(self.track, left)
        end = bisect.bisect_left(self.track, right)
		
        # range queried is inside the range of values being tracked
        return start == end and start % 2 == 1

        
        