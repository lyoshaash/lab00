#include <stdio.h>
#include <math.h>

int main()
{
     int x, y, z, n   ;
    printf("Enter x -> ");
    scanf("%d", &x);
    printf("Enter y -> ");
    scanf("%d", &y);
    printf("Enter z -> ");
    scanf("%d", &z);

    n = x;
    if (n < y) n = y;
    if (n < z) n = z;

    int sum = x + y + z - n;

    if (n > sum)
    {
     printf("Наибольшее число %d\n", n);
    }
    else 
    {
        int differ = sum - n;
        printf("Разность двух меньших параметров и большего равна %d\n", differ);
    }




}