/**
* Collin Franklin
* Programming Techniques
* 08-30-2024
*/

#include <iostream>

#define endl "\n"

using namespace std;

int main() {
    long B = 0, A = 0;

    while (cin >> A >> B) {

        if(A > B) {
            cout << A-B << endl;
        }
        else {
            cout << B-A << endl;
        }

    }
    return 0;
}
