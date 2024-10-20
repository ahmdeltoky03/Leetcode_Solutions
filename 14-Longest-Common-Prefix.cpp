class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
    string ans=\\\\;
     for(int i=0;i<strs[0].size();i++)
    {
        char x = strs[0][i];//a h m e d
        for(int g=0;g<strs.size();g++)
        {
            if(strs[g][i] != x)
            {
                return ans;
            }
        }
        ans+=x;
    }
    return ans;
        
    }
};