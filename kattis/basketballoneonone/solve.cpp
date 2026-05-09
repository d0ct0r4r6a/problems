#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    int A = 0;
    int B = 0;
    char curr = '-';
    for (char c : s) {
        if (c == 'A') {
            curr = 'A';
        } else if (c == 'B') {
            curr = 'B';
        } else {
            if (curr == 'A') {
                A += (int)c;
            } else if (curr == 'B') {
                B += (int)c;
            }
        }
    }
    cout << (A > B ? "A" : "B");
}