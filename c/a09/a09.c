#include <stdio.h>
#include <math.h>
#define SIZE 100

void magic(int num){
	int a[SIZE][SIZE] = {{0}};
	int border = (num / 2)*2;
	int requiredCalculations = pow(num,2) - 1;
	int i = 1;
	int x = num/2;
	int y = num/2;
	int cache;
	int j;
	int k;
	a[y][x] = 1;
	
	while(i<=requiredCalculations){
		
		/* feld links darunter innerhalb der border und inhalt noch leer*/
		if((y+1<=border) && (x-1>=0) && ((a[y+1][x-1]) == 0)){
			y+=1;
			x-=1;
			a[y][x] = i+1;
			printf("links unten leer\n");
			printf("i:%d, [%d][%d] = %d ", i, y,x, a[y][x]);
			
		}	
		/* feld links darunter innerhalb der border und inhalt bereits gefüllt und 
		 * x value innerhalb der border*/
		else if((y+1<=border) && (x-1>=0) && ((a[y+1][x-1]) != 0)){
			
			printf("links unten voll + ");
			/* 2 felder nach unten überschreitet die border */
			if(y+2>border){
				printf("zwei runter außerhalb der border\n");
				y+=2;
				y=y-border;
				y-=1;
				a[y][x] = i+1;
				printf("i:%d, [%d][%d] = %d \n", i, y,x, a[y][x]);
			/* 2 felder nach unten innerhalb der border */
			}else if(y+2<=border){
				printf("zwei runter innerhalb der border\n");
				y+=2;
				a[y][x] = i+1;
				printf("i:%d, [%d][%d] = %d \n", i, y,x, a[y][x]);
			}
				
		
		/* feld links darunter außerhalb der border, x und y umdrehen*/
		}else if((y+1)>border){
			/*cheesy evtl falsch */
			if(x!=y){
				cache = x;
				x = y;
				y = cache;
				a[y][x] = i+1;
				printf("links darunter außerhalb der border, x,y umdrehen");
				printf("i:%d, [%d][%d] = %d \n", i, y,x, a[y][x]);

			}
			/*cheesy, wenn nicht das rechts unterste xy=yx */
			else{
				x-=1;
				y=0;
				a[y][x] = i+1;
				printf("links darunter außerhalb der border, cheezy rechnen");
				printf("i:%d, [%d][%d] = %d \n", i, y,x, a[y][x]);

			}
		}
		printf("AFTER IF i:%d [%d][%d] = %d\n", i,y,x, a[y][x]);
		i++;
	}
	printf("\n");
	for(j=0; j< num; j++){
		for(k=0;  k< num; k++){
			printf("%d ", a[j][k]);
		}
		printf("\n");
	} 
	
}


int main (int argc, char *argv[]){
	int num;
	
	while(scanf("%d", &num), num % 2 == 1){
		magic(num);
	}
}
