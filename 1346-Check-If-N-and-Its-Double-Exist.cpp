class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        int sz = arr.size();
        // for(int i=0;i<sz;i++)if(arr[i]<0)arr[i]*=-1;
        // sort(arr.begin(),arr.end());
        for(int i=0;i<sz;i++){
            for(int j=0;j<sz;j++){
                if(i!=j && arr[j]==2*arr[i])return true;
            }
        }
        return false;
    }
};