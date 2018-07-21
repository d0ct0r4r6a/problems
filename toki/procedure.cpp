#include <iostream>
#include <string>

using namespace std;

string in;

void tulisJawaban(int bil)
{
  if (bil >= 1 && bil < 10)
  {
    cout << "satuan" << endl;
  }
  else if (bil >= 10 && bil < 100)
  {
    cout << "puluhan" << endl;
  }
  else if (bil >= 100 && bil < 1000)
  {
    cout << "ratusan" << endl;
  }
  else if (bil >= 1000 && bil < 10000)
  {
    cout << "ribuan" << endl;
  }
  else if (bil >= 10000 && bil < 100000)
  {
    cout << "puluhribuan" << endl;
  }
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
    tulisJawaban(stoi(in));
  }
  return 0;
}