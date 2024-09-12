class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        res = 0
        for i in range(len(students)):
            res += abs(seats[i]-students[i])
        return res
        """
        1 3 5
        2 4 7
        1+1+2
        -----
        2 2 6 6
        1 2 3 6
        1+0+3+0
        """