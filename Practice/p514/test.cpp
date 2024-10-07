#include <iostream>
#include <vector>
#include <stack>
#include <sstream>

using namespace std;

// Function to determine if the desired order can be achieved
string can_rearrange(int N, const vector<int>& desired_order) {
    stack<int> station;
    int current = 1;

    for (int coach : desired_order) {
        // Push coaches onto the stack until we find the desired coach
        while (current <= N) {
            station.push(current++);
        }
        // Check if the coach at the top of the stack matches the desired coach
        if (!station.empty() && station.top() == coach) {
            station.pop();
        } else {
            return "No";
        }
    }

    return "Yes";
}

// Function to process each block of input
void process_blocks(istream& in) {
    int N;
    while (in >> N && N != 0) {
        vector<string> results;
        in.ignore(); // To skip the newline after N

        string line;
        while (getline(in, line) && line != "0") {
            istringstream iss(line);
            vector<int> desired_order;
            int num;
            while (iss >> num) {
                desired_order.push_back(num);
            }
            results.push_back(can_rearrange(N, desired_order));
        }
        
        // Output the results for the current block
        for (const string& result : results) {
            cout << result << endl;
        }
        cout << endl; // Empty line after each block
    }
}

int main() {
    process_blocks(cin);
    return 0;
}

