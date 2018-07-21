#include <iostream>
#include <math.h>
using namespace std;

void cek_agak_prima(int bilangan)
{
  int banyak_faktor = 2;
  for (int n = 2; n <= pow(bilangan, 0.5); n++)
  {
    if (bilangan % n == 0)
    {
      if (bilangan / n == n)
      {
        banyak_faktor++;
      }
      else
      {
        banyak_faktor += 2;
      }
    }
    if (banyak_faktor > 4)
    {
      break;
    }
  }
  if (banyak_faktor <= 4)
    cout << "YA" << endl;
  else
    cout << "TIDAK" << endl;
}

int main()
{
  int T, bilangan;
  cin >> T;
  while (T--)
  {
    cin >> bilangan;
    cek_agak_prima(bilangan);
  }
  return 0;
}