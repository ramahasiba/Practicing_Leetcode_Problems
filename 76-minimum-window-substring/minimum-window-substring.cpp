#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        int s_length = s.length();
        int t_length = t.length();

        if (t_length > s_length) {
            return "";
        } else if (t == s) {
            return s;
        } 
        // else if (t_length == 1) {
        //     try {
        //         s.find(t);
        //         return t;
        //     } catch (...) {
        //         return "";
        //     }
        // }

        string ans = "";
        unordered_map<char, int> t_frequency;
        unordered_map<char, int> track;

        auto test = [&]() -> bool {
            for (const auto& entry : t_frequency) {
                if (entry.second > track[entry.first]) {
                    return false;
                }
            }
            return true;
        };

        // Initialize
        for (char c : t) {
            t_frequency[c]++;
            track[c] = 0;
        }

        int left_ptr = 0;
        int right_ptr = 0;
        int min_window_start = -1;
        int min_window_length = INT_MAX;

        for (int i = 0; i < s_length; ++i) {
            if (t_frequency.find(s[i]) != t_frequency.end()) {
                track[s[i]]++;
                while (test()) {
                    int current_window_length = i - left_ptr + 1;
                    if (current_window_length < min_window_length) {
                        min_window_length = current_window_length;
                        min_window_start = left_ptr;
                    }

                    // Move left
                    if (t_frequency.find(s[left_ptr]) != t_frequency.end()) {
                        track[s[left_ptr]]--;
                    }
                    left_ptr++;
                }
            }
        }

        if (min_window_start != -1) {
            ans = s.substr(min_window_start, min_window_length);
        }

        return ans;
    }
};
