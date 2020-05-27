#include <stdio.h>
#include <stdlib.h>

int main(void){
	
	int i;
	int a[1001];
	int b[1001];
	int c[1001];
	for (i=0;i<1001;i++){
		b[i] = i;
		c[i] = 2*i;
		a[i] = i;
#pragma omp parallel for default(none) private(i) reduction(+:sum) shared(a,b,c)
	i = omp_get_thread_num();
	if(i==1){
	{
	else if(i==2){
	}
}
