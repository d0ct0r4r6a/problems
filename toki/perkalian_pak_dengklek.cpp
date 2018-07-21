#include <iostream>
using namespace std;

char a[10], b[10];
int total = 0;

int main () {
  cin >> a >> b;
  for (int i = 0; i < 10; i++) {
    if (!a[i]) {
      break;
    }
    for (int j = 0; j < 10; j++) {
      if (!b[j]) {
        break;
      }
      int an = a[i] - '0';
      int bn = b[j] - '0';
      total += an * bn;
    }
  }
  cout << total << endl;
  return 0;
}