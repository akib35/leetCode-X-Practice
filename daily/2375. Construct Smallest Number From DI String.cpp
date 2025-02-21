#include <climits>
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string smallestNumber(string pattern) {
      return to_string(findSmallest(pattern,0,0,0));
    }
    
private:
    int findSmallest(string pattern, int idx, int msk, int num){
      if(idx==pattern.size()) return num;
      
      int res = INT_MAX;
      int lastdgt = num%10;
      bool sinc = idx==0||pattern[idx-1]=='I';
      
      for (int dig =1;dig<10;++dig){
        if( (msk & 1<<dig)==0 && (dig>lastdgt == sinc)){
          res = min(res, findSmallest(pattern, idx+1, msk|1<<dig, num*10+dig));
        }
      }
      return res;
    }
};

int main() {
    Solution solution;
    string pattern = "IIIDIDDD";
    string result = solution.smallestNumber(pattern);
    cout << result << endl;
    return 0;
}
