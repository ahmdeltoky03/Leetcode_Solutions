class Solution {
public:
    string makeGood(string s) {
      vector<char>arr;
      for(int i=0;i<s.size();i++){
        if(arr.empty())arr.push_back(s[i]);
        else if( s[i]-'a' == arr[arr.size()-1]-'A' || (s[i]-'A' == arr[arr.size()-1]-'a') )arr.pop_back();
        else arr.push_back(s[i]);
      }
      string res="";
    //   reverse(arr.begin(),arr.end());
      for(int i=0;i<arr.size();i++){
        res.append(string(1,arr[i]));
      }
      return res;
}
};
//leEeetcode
//0123456789