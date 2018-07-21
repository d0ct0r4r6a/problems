#include <iostream>
#include <string>
#include <math.h>
using namespace std;

int main() {
  string in;
  int a = -1;
  int b = -1;
  int bil_sekarang;
  int beda_terbesar = 0;
  while (1)
  {
    getline(cin, in);
    if (in.empty())
    {
      break;
    }
    bil_sekarang = stoi(in);
    if (a < 0) {
      a = bil_sekarang;
      continue;
    }
    if (b < 0) {
      b = bil_sekarang;
      beda_terbesar = abs(a - b);
      continue;
    }
    if (bil_sekarang < b) {
      if (a < b)
        a = bil_sekarang;
      else if (a >= b)
        b = bil_sekarang;
    } else if (bil_sekarang > a) {
      if (a <= b)
        b = bil_sekarang;
      else if (a > b)
        a = bil_sekarang;
    }
    if (abs(a - b) > beda_terbesar) {
      beda_terbesar = abs(a - b);
    }
  }
  cout << beda_terbesar << endl;
  return 0;
}