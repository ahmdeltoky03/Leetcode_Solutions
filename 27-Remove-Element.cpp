class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> num;
        // int i=0;
        sort(nums.begin(),nums.end());
        for(int g=0;g<nums.size();g++){
            
            if(nums[g] == val)continue;
            // i++;
            num.push_back(nums[g]);
        }
        nums.resize(num.size(),0);
        for(auto i =0 ;i<num.size();i++){
            nums[i]=num[i];
        }
        int k = nums.size();
        return k;
    }
};
//0 0 1 2 2 2 3 4
//0 0 1 3 4