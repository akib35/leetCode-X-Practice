#include <unordered_map>
#include <vector>
using namespace std;

class Solution {
public:
    long long countBadPairs(vector<int>& nums) {
        unordered_map<int, int> freq;
        long long good = 0, n = nums.size();
        
        for (int i = 0; i<n; i++) {
          int diff = nums[i] - i;
          good += freq[diff]++;
        }
        
        return n * (n - 1) / 2 - good;
    }
};