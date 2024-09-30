class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        _max = 0
        for account in accounts:
            _max = max(_max,sum(account))
        return _max
        