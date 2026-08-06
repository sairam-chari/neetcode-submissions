#include <queue>
using namespace std;

class Solution {
public:
    struct Compare {
        bool operator()(vector<int>& a, vector<int>& b) {
            return a[0]*a[0] + a[1]*a[1] < 
                   b[0]*b[0] + b[1]*b[1];
        }
    };

    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>, vector<vector<int>>, Compare> heap;

        for (auto& p : points) {
            heap.push(p);

            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<vector<int>> result;

        while (!heap.empty()) {
            result.push_back(heap.top());
            heap.pop();
        }

        return result;
    }
};
