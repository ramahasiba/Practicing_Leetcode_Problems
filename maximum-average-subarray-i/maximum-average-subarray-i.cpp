class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
    int list_length = nums.size();
    if (k > list_length) {
        return 0.0;  // Returning 0 as an indication of an invalid value for k
    }

    double max_average = 0.0;
    for (int i = 0; i < k; ++i) {
        max_average += nums[i];
    }
    double current_average = max_average;

    for (int i = k; i < list_length; ++i) {
        current_average += nums[i] - nums[i - k];
        max_average = std::max(max_average, current_average);
    }

    return max_average / k;
    }
}; 