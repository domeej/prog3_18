#include <stdio.h>
#include <string.h>



void printGap(int width, int amountOfGaps){
	int i,j; 
	int gap = width+amountOfGaps;
	width += 4;
	
	for(i=0; i < amountOfGaps; i++){
		for(j=0; j < gap; j++){
			if(j == 0 || j == gap-1){
				printf("*");
			}else{
				printf(" ");
			}
		}
		printf("\n");
	}
}

void printFull(int width, int amountOfGaps){
	int i = 0;
	width += 4;
	while(i < width){
		printf("*");
		i++;
	}
	printf("\n");
}


void printShizzl(char *s, int size){
	printf("länge:%ld\n",strlen(s));
	printf("%s, SIZE:%d\n", s, size);
	
	printFull(strlen(s),size);
	printGap(strlen(s),size);
	
	printf("*");
	printf(" %s ", s);
	printf("*\n");
	
	printGap(strlen(s),size);
	printFull(strlen(s), size);
	
	
	if(size>0){
		
	}
}


int main(int argc, char *argv[]){
	/* cc -Dsprache -DSIZE=abstand a18.c */
	char *s = "Ilman kuuloleitta en kuula mitaeaen";
	int size = 0;
	
	#if DE
		s = "Ohne Hoergeraet hoere ich nichts";
	#endif

	#if NL
		s = "Zonder gehoorapparaat hoor ik niets";
	#endif

	#if SE
		s = "Jag hoer ingenting utan hoerselapparat";
	#endif

	#if IT
		s = "Senza l’apparecchio d’autito non sento niente";
	#endif

	#if CN
		s = "mei zhu ting qi jiu tingbujian";
	#endif

	#if SIZE 
		size = SIZE;
	#endif 
	
	#ifndef SIZE
		size = 3;
	#endif
	
	printShizzl(s, size);
	
	
}
