// Example for getc() in C
#include <stdio.h>
int main()
{
  int a, b;
  scanf("%d%d", &a, &b);
  getchar();
  printf("%d", a + b);
  return (0);
}