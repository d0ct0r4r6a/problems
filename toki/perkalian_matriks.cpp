#include <iostream>
using namespace std;

int main()
{
  int rows1, cols1;
  int rows2, cols2;
  cin >> rows1 >> cols1;
  int matriks1[rows1][cols1];
  for (int i = 0; i < rows1; i++)
  {
    for (int j = 0; j < cols1; j++)
    {
      cin >> matriks1[i][j];
    }
  }
  cin >> rows2 >> cols2;
  int matriks2[rows2][cols2];
  for (int i = 0; i < rows2; i++)
  {
    for (int j = 0; j < cols2; j++)
    {
      cin >> matriks2[i][j];
    }
  }

  int matriksHasil[rows1][cols2];
  for (int currentRow = 0; currentRow < rows1; currentRow++)
  {
    for (int currentCol = 0; currentCol < cols2; currentCol++)
    {
      matriksHasil[currentRow][currentCol] = 0;
      for (int i = 0; i < cols1; i++)
      {
        matriksHasil[currentRow][currentCol] += matriks1[currentRow][i] * matriks2[i][currentCol];
      }
    }
  }
  for (int i = 0; i < rows1; i++)
  {
    for (int j = 0; j < cols2; j++)
    {
      cout << matriksHasil[i][j];
      if (j == cols2 - 1)
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