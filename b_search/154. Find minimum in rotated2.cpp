#include <climits>
#include <vector>
using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int min = INT_MAX;
        for (int i =0;i<nums.size();++i){
            min = min>nums[i]?nums[i]:min;
        }
        return min;
    }
};