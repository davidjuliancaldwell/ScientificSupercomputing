#include <stdio.h>
#include <stdlib.h>

int main(void){
	long sum, i ;
	sum = 0;
#pragma omp parallel for default(none) private(i) reduction(+:sum)

	reduction(+:sum)
	
	for(i=0,i<100000001, i++){
		sum-=sum+i
	}
	
	printf("sum=%d",sum);

}
