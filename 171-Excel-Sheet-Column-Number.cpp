class Solution {
public:
    int titleToNumber(string columnTitle) {
        reverse(columnTitle.begin(),columnTitle.end());
        long long sum=0,factor=1;
        for(int i=0;i<columnTitle.size();i++){
            sum += (columnTitle[i] - 'A' + 1 ) * factor ;
            factor *= 26;
        }
        // if(sum == 0)sum++;
        return sum;
    }
};