#include <iostream>
using namespace std;

int main()
{
  int A, B, C;
  int awal1, akhir1, awal2, akhir2, awal3, akhir3;
  int total_biaya = 0;
  int jumlah_truk = 0;
  cin >> A >> B >> C;
  cin >> awal1 >> akhir1 >> awal2 >> akhir2 >> awal3 >> akhir3;
  for (int i = 1; i <= 100; i++)
  {
    // Cek apakah truk 1 sedang parkir
    if (i >= awal1 && i + 1 <= akhir1)
    {
      jumlah_truk++;
    }
    // Cek apakah truk 2 sedang parkir
    if (i >= awal2 && i + 1 <= akhir2)
    {
      jumlah_truk++;
    }
    // Cek apakah truk 3 sedang parkir
    if (i >= awal3 && i + 1 <= akhir3)
    {
      jumlah_truk++;
    }
    // Hitung jumlah truk untuk menghitung
    // jumlah biaya untuk menit ini
    switch (jumlah_truk)
    {
    case 3:
      total_biaya += 3 * C;
      break;
    case 2:
      total_biaya += 2 * B;
      break;
    case 1:
      total_biaya += A;
      break;
    default:
      continue;
    }
    jumlah_truk = 0;
  }
  cout << total_biaya << endl;
  return 0;
}