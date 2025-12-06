#include <stdio.h>

int main() {
    int a1, a2, a3,a5;
    float a4;

printf("caso a) 9 +7 *8- 36/5 \n");
printf("ingrese el primer numero");
     scanf("%d",&a1);
printf("ingresa el segundo numero");
     scanf("%d",&a2);
printf("ingresa el tercer numero");
     scanf("%d",&a3);
 printf("ingrese el cuarto numero");
     scanf("%f",&a4);
printf("ingresa el quinto numero");
     scanf("%d",&a5);

 float resultado =a1+(a2*a3)-(a4/a5);

  printf("el resultado es: %.2f\n",resultado);

    return 0;
}
