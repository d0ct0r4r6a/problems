#include <iostream>
#include <string>
using namespace std;

int main()
{
  int n;
  string in;
  cin >> n;
  for (int i = 0; i < n; i++)
  {
    cin >> in;
    bool isLeadingZero = true;
    for (string::reverse_iterator rit = in.rbegin(); rit != in.rend(); ++rit)
    {
      if (*rit == '0' && isLeadingZero)
      {
        continue;
      }
      else
      {
        isLeadingZero = false;
        cout << *rit;
      }
    }
    if (isLeadingZero)
    {
      cout << 0;
    }
    cout << endl;
  }
  return 0;
}