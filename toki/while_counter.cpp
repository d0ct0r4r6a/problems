#include <iostream>
#include <sstream>
#include <string>
using namespace std;
int counter = 0;
string in;
int n;

int main()
{

  while (1)
  {
    getline(cin, in);
    if (in.empty())
    {
      break;
    }
    counter += stoi(in);
  }
  printf("%d\n", counter);
  return 0;
}