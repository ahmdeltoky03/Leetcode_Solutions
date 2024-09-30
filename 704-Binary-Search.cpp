class Solution {
public:
    int search(vector<int>& nums, int target) {
        bool is_exist = binary_search(nums.begin(),nums.end(),target);
        int idx = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        if(is_exist) {
            return idx;
        }
        else { 
            return -1;
        }
    }
};