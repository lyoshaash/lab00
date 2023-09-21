#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double x;

int main()
{
    
    double result;
    
    double s;
    printf("Enter s -> ");
    scanf("%lf", &s);

    for (x = 0.0; x <= 0.25; x+=s)
    {
        
            result = exp(sin(x));
            printf("%f %f\n", x, result);
        
        
    }

    for (x = 0.25; x <= 0.50; x+=s)
    {
        result = exp(x) - 1/sqrt(x);
        printf("%f %f\n", x, result);
    }

return 0;
}