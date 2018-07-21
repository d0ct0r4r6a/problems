#include <iostream>
using namespace std;

int main()
{
  int N;
  double in;
  double terkecil = 1000001.00;
  double terbesar = -1000001.00;
  double total = 0;
  cin >> N;
  for (int i = 0; i < N; i++)
  {
    cin >> in;
    if (in < terkecil)
    {
      terkecil = in;
    }
    if (in > terbesar)
    {
      terbesar = in;
    }
    total += in;
  }
  printf("%.2f %.2f %.2f\n", terkecil, terbesar, total / N);
  return 0;
}