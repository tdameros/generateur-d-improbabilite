#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *ft_strncat(char *dest, char *src, unsigned int nb);

int main(int argc, char *argv[])
{
    (void) argc;
    char dest[100];
    char *src = argv[2];
    strcpy(dest, argv[1]);
    printf("%s", ft_strncat(dest, argv[2], atoi(argv[3])));
    return (0);
}