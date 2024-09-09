class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        
        total_profit = 0
        max_profit = 0
        j = 0
        
        for w in worker:
            while j < len(jobs) and w >= jobs[j][0]:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            total_profit += max_profit
        
        return total_profit
