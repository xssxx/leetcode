#include <stdio.h> 
#include <ctype.h>

int filter(char* str) {
  char *read = str;
  char *write = str;

  int len = 0;

  while (*read != '\0') {
    if (isalnum(*read)) {
      *write = tolower(*read);
      write++;
      len++;
    }
    read++;
  }
  *write = '\0';

  return len;
}

int main() {
  char str[] = "Hello!, I love C!!";
  int len = filter(str);

  int i = 0, j = len - 1;

  int flag = 1;
  while (i < len) {
    if (str[i] != str[j]) {
      flag = 0;
      break;
    }
    i++; j++;
  }

  if (flag)
    printf("str is palindrome");
  else
    printf("str is not palindrome");

  return 0;
}
