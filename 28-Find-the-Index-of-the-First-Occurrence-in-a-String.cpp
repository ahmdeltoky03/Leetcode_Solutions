class Solution {
public:
    int strStr(string haystack, string needle) {
        bool isFound = haystack.find(needle) != string::npos;
        int temp=0;
        if(isFound){
            int g=0;
            for(int i=0;i<haystack.size();i++){
                int ii=i;
                while(g < needle.size()){
                     if(needle[g] == haystack[ii]){
                        ii++;
                        g++;
                     }
                     else break;
                }
                if(g == needle.size()){
                    temp = i;
                    break;
                }
                else{
                    g = 0;
                }
            }
        }
        else{
            return -1;
        }
        return temp;
        }
    
};