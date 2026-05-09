#include<iostream>

using namespace std;

int main() {
    freopen("1.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    string r;
    cin >> r;
    cout << r[r.size() - 2];
}