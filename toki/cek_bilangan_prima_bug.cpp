#include <iostream>
#include <string>
#include <math.h>
using namespace std;

string in;

void cek_prima(int bilangan)
{
  string jawaban = "YA";
  if (bilangan < 2)
  {
    jawaban = "TIDAK";
  }
  for (int i = 2; i < pow(bilangan, 0.5); i++)
  {
    if (bilangan % i == 0)
    {
      jawaban = "TIDAK";
      break;
    }
  }
  cout << jawaban << endl;
}

int main()
{
  while (1)
  {
    getline(cin, in);
    if (in.empty())
    {
      break;
    }
    cek_prima(stoi(in));
  }
  return 0;
}
