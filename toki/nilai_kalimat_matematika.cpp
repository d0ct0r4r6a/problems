#include <iostream>
using namespace std;

void hitung_nilai(int A, char op, int B)
{
  switch (op)
  {
  case '+':
    cout << A + B;
    cout << endl;
    break;
  case '-':
    cout << A - B;
    cout << endl;
    break;
  case '*':
    cout << A * B;
    cout << endl;
    break;
  case '<':
    if (A < B)
      cout << "benar";
    else
      cout << "salah";
    cout << endl;
    break;
  case '>':
    if (A > B)
      cout << "benar";
    else
      cout << "salah";
    cout << endl;
    break;
  case '=':
    if (A == B)
      cout << "benar";
    else
      cout << "salah";
    cout << endl;
    break;
  default:
    cout << "invalid";
  }
}

int main()
{
  int A, B;
  char op;
  cin >> A >> op >> B;
  hitung_nilai(A, op, B);
  return 0;
}