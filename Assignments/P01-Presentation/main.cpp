#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
    int testcase;
    cin >> testcase;

    while (testcase--) {
        int n;
        cin >> n;

        vector<pair<int, int>> points(n);
        for (int i = 0; i < n; ++i) {
            cin >> points[i].first >> points[i].second;
        }

        // Find min and max of x-coordinates
        int mx = points[0].first, mn = points[0].first;
        for (const auto& p : points) {
            mx = max(mx, p.first);
            mn = min(mn, p.first);
        }

        // Calculate the midpoint
        double mid = (mx + mn) / 2.0;

        // Set to store transformed (x', y) points
        set<pair<int, int>> transformedPoints;
        for (const auto& p : points) {
            int transformedX = static_cast<int>((p.first - mid) * 2);
            transformedPoints.emplace(transformedX, p.second);
        }

        bool isSymmetric = true;
        for (const auto& p : points) {
            int reflectedX = static_cast<int>(-(p.first - mid) * 2);
            if (transformedPoints.find({reflectedX, p.second}) == transformedPoints.end()) {
                isSymmetric = false;
                break;
            }
        }

        // Output the result
        cout << (isSymmetric ? "YES" : "NO") << endl;
    }

    return 0;
}
