#include <iostream>
using namespace std;

int a, b;

void swap(int &a, int &b)
{
  int temp;
  temp = a;
  a = b;
  b = temp;
}

int main()
{
  cin >> a >> b;
  swap(a, b);
  cout << a << ' ' << b << endl;
  return 0;
}