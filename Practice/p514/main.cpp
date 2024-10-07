#include <iostream>
#include <vector>

using namespace std;

void print(vector<int> v);

int main () {

    int N,j,c;
    vector<int> inwagons;
    vector<int> outwagons;
    vector<int> station;

    cin >> c;
    
    while(c) {
        N = c;
        while (j) {
            cin >> j;
            while(c--)
            if (j == 0) {
                break;
            }
        inwagons.push_back(j);
        }
    }
}
void print(vector<int> v) {
    for(auto &N : v) {
        cout << N << endl;
    }
}
