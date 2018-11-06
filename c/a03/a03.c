#include <stdio.h>

void getNumber(int n);

int main (int argc, char *argv[]){
	int nr;
	scanf("%d", &nr);  
	getNumber(nr);
	
	return 0;
}


void getNumber(int n){
	int hundred = 100;
	int fifty = 50;
	int ten = 10;
	int five = 5;
	int amount = 0;
	
		while ((n / hundred)>=1){
			amount = n / hundred;
			for(int i = 0; i < amount; i++){
				printf("C"); 
			}
			n = n%hundred;
		}
		while ((n / fifty)>=1){
			amount = n / fifty;
			for(int i = 0; i < amount; i++){
				printf("L"); 
			}
			n = n%fifty;
		}
		while ((n / ten)>=1){
			amount = n / ten;
			for(int i = 0; i < amount; i++){
				printf("X"); 
			}
			n = n%ten;
		}
		while ((n / five)>=1){
			amount = n / five;
			for(int i = 0; i < amount; i++){
				printf("V"); 
			}
			n = n%five;
		}
		while ((n / 1)>=1){
			amount = n / 1;
			for(int i = 0; i < amount; i++){
				printf("I"); 
			}
			n = n%1;
		}
}
