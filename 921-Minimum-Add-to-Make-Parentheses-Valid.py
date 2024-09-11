class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        for i in s:
            if str(i) == "(":
                st.append("(")

            else:
                if str(i) == ")" and len(st) != 0:
                    if st[-1] == "(":
                        st.remove(st[-1])
                    else:
                        st.append(")")
                else:
                    st.append(i)
        return len(st)