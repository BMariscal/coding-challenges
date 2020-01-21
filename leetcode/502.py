import heapq
class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        L = len(Profits)
        cache = []
        for i in range(L):
            cache.append((Capital[i], Profits[i]))
        cache.sort(key = lambda x: x[0]) # O(NlogN)
        pq = []
        index = 0
        while k: # O(NlogN) since we use 'index' to track the position, we only need to loop 'cache' once
            for i in range(index, L):
                if cache[i][0] <= W:
                    heapq.heappush(pq, (-cache[i][1]))
                    index = i+1
                else:
                    break
            if not pq:
                break
            W += -heapq.heappop(pq)
            k -= 1
        return W