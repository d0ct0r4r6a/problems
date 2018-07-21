#include <iostream>
using namespace std;

int bil[1001];

int main()
{
  int n;
  for (int i = 0; i < 1001; i++)
  {
    bil[i] = 0;
  }

  cin >> n;
  for (int i = 0; i < n; i++)
  {
    int number;
    cin >> number;
    bil[number]++;
  }

  int modusTerbesar = 1;
  for (int i = 2; i < 1001; i++)
  {
    if (bil[i] >= bil[modusTerbesar])
    {
      modusTerbesar = i;
    }
  }
  cout << modusTerbesar << endl;
  return 0;
}