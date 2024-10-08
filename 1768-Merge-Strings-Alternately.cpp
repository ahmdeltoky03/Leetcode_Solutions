class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int i=0,g=0;
        string merged="";
        while(i<word1.length() || g<word2.length()){
            if(i<word1.length()){
                merged+=word1[i];
                i++;
            }
            if(g<word2.length()){
                merged+=word2[g];
                g++;
            }
        }
        return merged;
    }
};