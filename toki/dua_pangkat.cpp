#include <iostream>
using namespace std;

void cek_dua_pangkat(int bilangan)
{
  while (bilangan > 1)
  {
    if (bilangan % 2 != 0)
    {
      cout << "FALSE" << endl;
      return;
    }
    bilangan = bilangan / 2;
  }
  cout << "TRUE" << endl;
}

int main()
{
  int in;
  cin >> in;
  cek_dua_pangkat(in);
  return 0;
}