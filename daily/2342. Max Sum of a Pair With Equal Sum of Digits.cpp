// #include <vector>
// #include <unordered_map>
// #include <algorithm>

// TLE solution
// class Solution {
// public:
//     int maximumSum(std::vector<int>& nums) {
//         int maxSum = -1;
//         for (int i=0;i<nums.size();i++) {
//             for (int j=i+1;j<nums.size();j++) {
//                 if (digitSum(nums[i]) == digitSum(nums[j])) {
//                     maxSum = max(maxSum, nums[i] + nums[j]);
//                 }
//             }
//         }

//         return maxSum;
//     }

// private:
//     int digitSum(int num) {
//         int sum = 0;
//         while (num > 0) {
//             sum += num % 10;
//             num /= 10;
//         }
//         return sum;
//     }
// };

class Solution {
public:
    int maximumSum(vector<int>& nums) {
        unordered_map<int, vector<int>> digitSumMap;
        for( int num : nums ) {
            int sum = sumOfDigits( num );
            digitSumMap[sum].push_back( num );
        }
        int maxSum = -1;
        for( auto& [sum,group] : digitSumMap ) {
            if( group.size() > 1 ) {
              sort(group.begin(),group.end(),greater<int>());
              maxSum = max( maxSum, group[0] + group[1] );
            }
        }
        return maxSum;
    }
private:
    int sumOfDigits( int num ) {
        int sum = 0;
        while( num > 0 ) {
          sum += num % 10;
          num /= 10;
        }
        return sum;
    }
};
