#include <stdio.h>
#include <math.h>
#include <stdlib.h>

double f;
double x;


int main()
{
    
    double x = 0.0;
    double result;
    
    double s;
    printf("Enter s -> ");
    scanf("%lf", &s);



    do {
        
        if (x>=0 && x <= 0.25) {
            result = exp(sin(x));
            printf("%f %f\n", x, result);
        }
        x += s;

    }while (x <= 0.25);
    
    do {
        
        if (x>0.25 && x <= 0.5) {
            result = exp(x)- 1/sqrt(x);
            printf("%f %f\n", x, result);
        }
        x += s;


    }while (x <=0.5);
return 0;
}


