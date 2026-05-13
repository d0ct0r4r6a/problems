#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    freopen("paint.in", "r", stdin);
    freopen("paint.out", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(nullptr);

    int a, b, c, d;
    cin >> a >> b >> c >> d;
    if (c >= a && c <= b || d >= a && d <= b || a >= c && a <= d || b >= c && b <= d) {
        int minVal = min({a, b, c, d});
        int maxVal = max({a, b, c, d});
        cout << maxVal - minVal;
    } else {
        cout << (b - a + d - c);
    }
}