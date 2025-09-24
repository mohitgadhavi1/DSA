from collections import deque, defaultdict
import bisect

class Router(object):

    def __init__(self, memoryLimit):
        """
        :type memoryLimit: int
        """
        self.memoryLimit = memoryLimit
        self.queue = deque()
        self.seen = set()
        self.dest_map = defaultdict(list)



    def addPacket(self, source, destination, timestamp):
        """
        :type source: int
        :type destination: int
        :type timestamp: int
        :rtype: bool
        """
        packet = (source,destination,timestamp)
        if packet in self.seen:
            return False
        
        # Evict oldest if memory full
        if len(self.queue) == self.memoryLimit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.seen.remove((old_source, old_dest, old_time))
            # remove old_time from dest_map[old_dest]
            idx = bisect.bisect_left(self.dest_map[old_dest], old_time)
            if idx < len(self.dest_map[old_dest]) and self.dest_map[old_dest][idx] == old_time:
                self.dest_map[old_dest].pop(idx)
            if not self.dest_map[old_dest]:
                del self.dest_map[old_dest]
        # Add new packet
        self.queue.append(packet)
        self.seen.add(packet)
        self.dest_map[destination].append(timestamp)  # timestamps always increasing
        return True

    def forwardPacket(self):
        """
        :rtype: List[int]
        """
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.seen.remove((source, destination, timestamp))
        # remove timestamp from dest_map[destination]
        idx = bisect.bisect_left(self.dest_map[destination], timestamp)
        if idx < len(self.dest_map[destination]) and self.dest_map[destination][idx] == timestamp:
            self.dest_map[destination].pop(idx)
        if not self.dest_map[destination]:
            del self.dest_map[destination]
        return [source, destination, timestamp]
        

    def getCount(self, destination, startTime, endTime):
        """
        :type destination: int
        :type startTime: int
        :type endTime: int
        :rtype: int
        """
        if destination not in self.dest_map:
            return 0
        timestamps = self.dest_map[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)