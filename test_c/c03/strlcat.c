#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[])
{
    (void) argc;
    char dest[100];
    char *src = argv[2];
    strcpy(dest, argv[1]);
    printf("%d\t%s", strlcat(dest, argv[2], atoi(argv[3])), dest);
    return (0);
}