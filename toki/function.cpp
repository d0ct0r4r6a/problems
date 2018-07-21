#include <iostream>
using namespace std;

bool valid(int n)
{
  return (n >= 0 && n <= 10);
}

int faktorial(int n)
{
  if (n == 0)
  {
    return 1;
  }
  else
  {
    return n * faktorial(n - 1);
  }
}

int main()
{
  int n;
  scanf("%d", &n);
  if (valid(n))
  {
    cout << faktorial(n) << endl;
  }
  else
  {
    cout << "ditolak" << endl;
  }
  return (0);
}