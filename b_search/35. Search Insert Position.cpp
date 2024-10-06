#include <vector>
using namespace std;
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
      int left = 0, right = nums.size() - 1, mid = 0;
      while(left<=right){
        mid = (left+right)>>1;
        if(nums[mid] == target) return mid;
        else if(nums[mid] < target) left = mid + 1;
        else right = mid - 1;
      }
      return left;
    }
};