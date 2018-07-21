#include <iostream>

using namespace std;

int main()
{

  int a, b, c, d, data1[75][75], data2[75][75];

  scanf("%d%d", &a, &b);
  for (int i = 0; i < a; i++)
  {
    for (int j = 0; j < b; j++)
    {
      scanf("%d", &data1[i][j]);
    }
  }

  scanf("%d%d", &c, &d);
  for (int i = 0; i < c; i++)
  {
    for (int j = 0; j < d; j++)
    {
      scanf("%d", &data2[i][j]);
    }
  }

  for (int i = 0; i < a; i++)
  {
    for (int j = 0; j < d; j++)
    {
      int z = 0;
      for (int k = 0; k < b; k++)
      {
        z += data1[i][k] * data2[k][j];
      }
      printf("%d", z);
      if (j != b)
        printf(" ");
    }
    printf("\n");
  }
  return 0;
}