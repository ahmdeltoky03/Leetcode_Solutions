class Solution {
public:
    int compareVersion(string version1, string version2) {
        int i=0,g=0,v_1,v_2,n=0,m=0;
        v_1=version1.size();
        v_2=version2.size();
        while(i<v_1 || g<v_2){
            while(i < v_1 && version1[i] != '.'){
                n = n * 10 + (version1[i] - '0');
                i++;
            }
            while(g < v_2 && version2[g] != '.'){
                m = m * 10 + (version2[g] - '0');   
                g++;
            }
         if(n < m) return -1;
        else if(n > m) return 1;   
        g++,i++;
        n = 0,m=0;
        }
        
        return 0;
    }
};