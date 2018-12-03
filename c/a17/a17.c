#include <stdio.h>

int main(int argc, char *argv[]){
	int mem[2] = {0};
	
	
	printf("%ld\n", sizeof(double));
	sscanf(argv[1], "%lf", &mem);
}
