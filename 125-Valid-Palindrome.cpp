class Solution {
public:
    bool isPalindrome(string s) {
        int ln = s.size();
        if (ln == 0)return true;
        string ss = "";
        for(int i=0;i<ln;i++){
            if(s[i]>='A'&&s[i]<='Z')ss+=(s[i]+32);
            else if(s[i]>='a'&&s[i]<='z')ss+=s[i];
            else if(s[i]>='0' && s[i]<='9')ss+=s[i];
            else continue;
        }
        for(int i=0;i<ss.size()/2;i++){
            if(ss[i] != ss[ss.size()-i-1])return false;
        }
        return true;
    }
};