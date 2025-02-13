#include <vector>
#include <algorithm>
#include <iostream>
#include <queue>
using namespace std;

class Solution
{
public:
    void printMinHeap(priority_queue<int, vector<int>, greater<int>> minHeap)
    {
        while (!minHeap.empty())
        {
            cout << minHeap.top() << " ";
            minHeap.pop();
        }
        cout << endl;
    }

    int minOperationsToExceedThreshold(vector<int> &nums, int threshold)
    {
        priority_queue<int, vector<int>, greater<int>> minHeap(nums.begin(), nums.end());
        int operations = 0;

        while (minHeap.size() > 1)
        {
            long long first = minHeap.top();
            minHeap.pop();
            long long second = minHeap.top();
            minHeap.pop();

            if (first >= threshold)
                break;

            // Correct the calculation to prevent overflow
            long long sum = first * 2 + second;
            minHeap.push(sum);
            operations++;
            printMinHeap(minHeap);
        }

        // Check if the last element in the heap exceeds the threshold
        if (!minHeap.empty() && minHeap.top() >= threshold)
        {
            return operations;
        }

        return operations; // Return the number of operations performed
    }
};

int main()
{
    Solution solution;
    vector<int> nums = {1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999};
    int threshold = 1000000000;
    int result = solution.minOperationsToExceedThreshold(nums, threshold);
    cout << "Minimum operations: " << result << endl;
    return 0;
}

// It doesn't work for long long ++ values.
// Hence python code:
// import heapq

// class Solution:
//     def print_min_heap(self, min_heap):
//         # Print the elements of the min-heap
//         while min_heap:
//             print(heapq.heappop(min_heap), end=" ")
//         print()

//     def min_operations_to_exceed_threshold(self, nums, threshold):
//         # Create a min-heap from the input list
//         min_heap = nums[:]
//         heapq.heapify(min_heap)
//         operations = 0

//         while len(min_heap) > 1:
//             first = heapq.heappop(min_heap)
//             second = heapq.heappop(min_heap)

//             if first >= threshold:
//                 break

//             # Correct the calculation to prevent overflow
//             sum_value = first * 2 + second
//             heapq.heappush(min_heap, sum_value)
//             operations += 1
//             self.print_min_heap(min_heap)

//         # Check if the last element in the heap exceeds the threshold
//         if min_heap and min_heap[0] >= threshold:
//             return operations

//         return operations  # Return the number of operations performed

// # Example usage
// if __name__ == "__main__":
//     solution = Solution()
//     nums = [1000000000, 999999999, 1000000000, 999999999, 1000000000, 999999999]
//     threshold = 1000000000
//     result = solution.min_operations_to_exceed_threshold(nums, threshold)
//     print("Minimum operations:", result)
