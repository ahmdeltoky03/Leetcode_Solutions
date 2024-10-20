class Solution {
public:
    int findMaxK(vector<int>& nums) {
        int max = -1001;
        map<int,int>mp;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size();i++)
        {
           mp[nums[i]]++;
        }
        for(int i=0;i<nums.size();i++)
        {
           if(mp[nums[i]] && mp[-nums[i]])
              max = nums[i];
        }
    
        if(max == -1001)
        return -1;
        else
        return max;
    }
};

//-3 -1 2 3