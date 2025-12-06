#include <stdio.h>

int main() {
   int a;
    int result;
    int result2;

    printf("ingresa un numero ");
    scanf("%d",&a);

    result = a *a ;
    result2 = a *a*a ;
    printf("el total es %d\n",result);
    printf("el total es %d\n",result2);

    return 0;
}
