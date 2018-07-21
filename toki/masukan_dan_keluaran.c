// Example for getc() in C
#include <stdio.h>
int main()
{
  char words[100];
  // scanf("%s", words); // this works for string without space
  fgets(words, 100, stdin);
  printf("%s", words);
  return (0);
}