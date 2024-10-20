class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
       sort(people.begin(),people.end());
       int i=0,g=people.size()-1,ans=0;
       while(i<=g){
        // ans += 1;
        if(people[i]+people[g] <= limit){
           ans++;
           i++;
        }
        else{
           ans++; 
        }
        g--;
       }
       return ans;
    }
};
//1 2 2 3 || limit = 3
//