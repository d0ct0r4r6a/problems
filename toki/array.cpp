#include <iostream>
#include <string>
using namespace std;

int bil[25000];
int index = 0;
string in;

int main()
{
  while (1)
  {
    getline(cin, in);
    if (in.empty())
    {
      break;
    }
    bil[index++] = stoi(in);
  }
  for (int i = index - 1; i > -1; i--)
  {
    cout << bil[i] << endl;
  }
  return 0;
}