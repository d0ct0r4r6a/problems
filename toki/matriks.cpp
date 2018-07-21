#include <iostream>
using namespace std;

int main()
{
  int n, m;
  cin >> n >> m;
  int matriks[n][m];
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
    {
      cin >> matriks[i][j];
    }
  }
  for (int i = 0; i < m; i++)
  {
    for (int j = n - 1; j > -1; j--)
    {
      cout << matriks[j][i];
      if (j == 0)
      {
        cout << endl;
      }
      else
      {
        cout << ' ';
      }
    }
  }
  return 0;
}
