#include <stdio.h>
#include <stdlib.h>

int main(void){

const int MAX=6000;
int i;
int sum;

//initialize i and sum
sum = 0;
i = 1;

while(i<MAX+1){
	sum=sum+i;
//	sleep(1);
	i=i+1;
}

printf("%d\n",sum);
fflush(stdout);

}
