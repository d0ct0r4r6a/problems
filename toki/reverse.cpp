#include <iostream>
#include <string>
using namespace std;

int main()
{
  string in;
  getline(cin, in);
  for (string::reverse_iterator rit = in.rbegin(); rit != in.rend(); ++rit)
  {
    cout << *rit;
  }
  cout << endl;
  return 0;
}
