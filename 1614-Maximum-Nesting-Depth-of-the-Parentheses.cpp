class Solution {
public:
    int maxDepth(string s) {
        int ans=-100000,left=0,right=0;
        for(int i=0;i<s.size();i++){
            if(s[i] == '(')left++;
            else if(s[i] == ')')right++;
            ans=max(left-right,ans);

        }

                return ans;

        }
};