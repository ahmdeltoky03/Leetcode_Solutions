class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        res = 0
        for oper in operations:
            if oper in ["X++","++X"]:
                res += 1
            else:
                res -= 1
        return res
        