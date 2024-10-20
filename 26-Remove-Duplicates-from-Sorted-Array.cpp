class Solution {
public:
    int removeDuplicates(vector<int>& arr) {
        map<int,int>mp;
        for(int i=0;i<arr.size();i++)
        {
            if(!mp[arr[i]])mp[arr[i]]++;
        }
        int size=arr.size();
        arr.resize(mp.size());
        int i=0;
        for(auto [a,b] : mp){
            arr[i]=a;
            i++;
        }
        return i;
    }
};