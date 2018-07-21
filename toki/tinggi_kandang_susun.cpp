#include <iostream>
#include <math.h>
using namespace std;

int main () {
  int N, K, tertinggi = 0, tinggi_kucing_k;
  long long int total_tinggi = 0;
  cin >> N >> K;
  for (int i = 1; i <= N; i++) {
    cin >> tinggi_kucing_k;
    if (tinggi_kucing_k > tertinggi) {
      tertinggi = tinggi_kucing_k;
    }
    if (i % K == 0) {
      total_tinggi += tertinggi;
      tertinggi = 0;
    }
  }
  if (tertinggi > 0) {
    total_tinggi += tertinggi;
  }
  if (N > K) {
    total_tinggi += ceil((double)N / K) + 1;
  } else {
    total_tinggi += 2;
  }
  cout << total_tinggi << endl;
  return 0;
}