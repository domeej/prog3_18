#include <stdio.h>
#include <string.h>

#define SIZE 100

int* selectionSort(int *a, int len){
	int i, smallest, first, cache;
	
	first = 0;
	while(first<len){
		smallest = first;
		for(i = first; i<len; i++){
			if(a[i] < a[smallest]){
				smallest = i;
			}
		}
		cache = a[first];
		a[first] = a[smallest];
		a[smallest] = cache;
		first++;	
	}
	return a;
}


int main (int argc, char *argv[]){
	int input[SIZE];
	int *res;
	int i, len;
	i = 0;
	
	while(scanf("%d", &input[i]) != EOF){
		i++;
	}
	len = i;
	res = selectionSort(input, len);
	
	for(i = 0; i<len; i++){
		printf("%d ", res[i]);
	}
}


