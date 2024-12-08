class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return False
        temp = [rooms[0]]
        visited = set()
        visited.add(0)
        q = collections.deque(temp)
        res = []
        while(q):
            curr = q.popleft()
            for i in curr:
                if i not in visited:
                    q.append(rooms[i])
                    visited.add(i)
        
        if len(rooms) == len(visited):
            return True
        return False
