class Solution {
public:
    int arrangeCoins(int n) {
        long long  i = 1, cnt = 1,temp=2;
    while (i <= n) {
        if(i+temp <= n) {
            cnt++;
            i+=temp;
            temp++;
        }
        else {
            break;
        }
    }
    return cnt;
    }
};