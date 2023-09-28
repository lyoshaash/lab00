#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[])
{
    int i;
    int c;
    c = rand ();
    for (i = 0; i < n; i++)
        a[i] = rand () % ((2 * c) + 1) - c;
}

int main()
{
    srand(time(NULL));
    int n;
    printf("n -> ");
    scanf("%d", &n);
    int A[n];
    fill(n, A);
    int neg_arr[n];
    int pos_arr[n];
    int neg_it = 0;
    int pos_it = 0;
    for(int i = 0; i < n; i++) {
        if(A[i] < 0) {
            neg_arr[neg_it++] = A[i];
        }
        else {
            pos_arr[pos_it++] = A[i];
        }
    }
    int i;
    for (i = 0; i < pos_it; i++)
        printf("%5d ", pos_arr[i]  );
    printf("\n");
    for (i = 0; i < neg_it; i++)
        printf("%5d ", neg_arr[i]  );
    printf("\n"); 
    return 0;
}
