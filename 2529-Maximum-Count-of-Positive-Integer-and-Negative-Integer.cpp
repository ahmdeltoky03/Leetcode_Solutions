class Solution {
public:
    int maximumCount(vector<int>& nums) {
        int neg = 0,pos = 0;
        for(auto it : nums){
            if(it > 0)pos++;
            else if ( it < 0)neg++;
        }
        return max(neg,pos);
    }
};