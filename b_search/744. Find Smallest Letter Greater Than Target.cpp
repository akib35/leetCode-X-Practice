#include <vector>
using namespace std;
class Solution {
public:
  char nextGreatestLetter(vector<char> &letters, char target) {
    int left = 0, right = letters.size(), mid = 0;
    while(left<right){
      mid = (left+right)>>1;
      if(letters[mid] <= target) left = mid + 1;
      else right = mid;
    }
    return left == letters.size() ? letters[0] : letters[left];
  }
};
