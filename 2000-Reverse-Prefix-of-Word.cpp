class Solution {
public:
    string reversePrefix(string word, char ch) {
        bool flag =false;
        int index = 0;
        for(int i=0;i<word.size();i++){
            if(word.at(i) == ch){
                index = i;
                flag = true;
                break;
            }
        }
        if(flag){
            reverse(word.begin()+0,word.begin()+index+1);
        }    
        return word;
        }
    
};
//abcdefd
//dcb