class Solution {
public:
    int lengthOfLastWord(string s) {
        string ans="";
        for(int i=s.size()-1;i>=0;i--){
           if(ans == "" && s.at(i) == 32)continue;
           if(ans != "" && s.at(i) == 32)break;;
           ans+=s.at(i);
        }
        return ans.size();
    }
};