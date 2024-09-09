class Solution {
public:
    int romanToInt(string s) {
        int ans=0;
        map<char,int>mp;
        mp['I']=1,
        mp['V']=5,
        mp['X']=10,
        mp['L']=50,
        mp['C']=100,
        mp['D']=500,
        mp['M']=1000;
        //0123456
        //MCMXCIV
        for(int i=0;i<s.size();i++){
            if(mp[s[i]]-mp[s[i+1]] >= 0)ans+=mp[s[i]];
            else {
                ans+=mp[s[i+1]]-mp[s[i]];
                i++;
            }
        }
        // int size=s.size();
        // if(mp[s[size-2]]-mp[s[size-1]] >= 0)ans+=mp[s[size-1]];
        return ans;
    }
};