class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for ( int i = 0; i < nums.size(); i++ ){
        	int required = target - nums[i];
        	for ( int j = i + 1; j < nums.size(); j++ ) {
        		if (nums[j]==required) return {i,j};
        	}
        	
        }
        return {};
    }
};

//python
//class Solution:
//    def twoSum(self, nums: List[int], target: int) -> List[int]:
//        hashmap = {}
//        for i in range(len(nums)):
//            comp = target - nums[i]
//            if comp in hashmap:
//                return [i,hashmap[comp]]
//            hashmap[nums[i]] = i
//        return []
