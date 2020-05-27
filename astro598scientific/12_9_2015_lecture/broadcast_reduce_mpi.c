// broadcast_reduce_mpi.c
// sum integers from 1 to MAX

#include <stdio.h>
#include <stdlib.h>
#include "mpi.h"

main(int argc, char** argv) {
	int my_rank; // my process rank
	int p; //the number of processes
	int MAX; // we choose only multiple of 16 to keep code simple.
		// Since each node has 16 cores
		// this ensures that delta=MAX/p is an integer 
	
	int local_min;
	int local_max;
	int delta;
	int i;

	int local_sum;
	int total_sum;
	int source; //process sending local_sum
	int dest = 0;
	int tag = 0;
	MPI_Status status;

	MPI_Init(&argc, &argv);
	
	//Get my proces rank
	MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

	//Find out how many processes are being used
	MPI_Comm_Size(MPI_COMM_WORLD, &p);

	if(my_rank = 0){
		MAX = 16000;
		printf("p=%d\n",p);
	}

	MPI_Bcast(&MAX, 1, MPI_INT, 0, MPI_COMM_WORLD);

	if( MAX % p !=0){
		printf("MAX=%d is not divisible by number of processors p=%d\n", MAX, p);
		exit(1);
	}

	if( MAX < p){
		printf("MAX=%d is less than number of processors p=%d\n", MAX, p);
		exit(2);
	}

	delta = MAX/p;

	local_min=my_rank*delta+1;
	local_max=(my_rank+1)*delta;

	local_sum=0;
	for(i=local_min;i<=local_max;i++){
		local_sum=local_sum+1;
	}

	MPI_Reduce(&local_sum, &total_sum, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

	if (my_rank == 0) {
		printf("sum from 1 to %d = %d\n", MAX, total_sum);
	}

	MPI_Finalize();

}
//end main
