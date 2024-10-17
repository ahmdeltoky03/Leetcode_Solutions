class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char,int>mp1,mp2;
        s.erase(unique(s.begin(),s.end()),s.end());
        t.erase(unique(t.begin(),t.end()),t.end());
        if(t.size()-s.size())return false;
        for(int i=0;i<s.size();i++)mp1[s[i]]++;
        for(int i=0;i<t.size();i++)mp2[t[i]]++;
        for(int i=0;i<s.size();i++){
            if(mp1[s[i]]!=mp2[t[i]])return false;
        }
        return true;

    }
};