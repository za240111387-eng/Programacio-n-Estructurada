#include <stdio.h>

int main() {
     float a;
     float b;
    float result;
    float result2;


    printf("Cuantos kilometros? : ");
    scanf("%f",&a);

    result = a * 1000;
   result2=a*100000;
    printf("en metros es %f\n",result);
  printf("en centimetros es %f\n",result2);
    return 0;
}
