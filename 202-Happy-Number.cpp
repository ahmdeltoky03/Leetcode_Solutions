class Solution {
public:
    bool isHappy(int n) {
        if(n == 1 || n == 7) return true;
        else if(n<10&&n!=1)return false;
        int num=0,sum=0;
        while(n){
            int temp=n%10;
            sum += (int)pow(temp,2);
            n/=10;
        }
        return isHappy(sum);
    }
};