class Solution {
public:
    int numberOfMatches(int n) {
       int NumMatches=0;
       while(n > 1){
        if(n % 2 == 0){
            NumMatches+=n/2;
            n/=2;
        }
        else{
            NumMatches+=(n - 1)/2;
            n = ((n-1)/2) + 1;
        }
       } 
    return NumMatches;
    }
};