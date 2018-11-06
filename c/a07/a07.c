#include <stdio.h>
#include <string.h>
#include <math.h>

void schreibbit(unsigned z){
	int counter = 16;

	while(counter >= 0){
		if ((z & (1<<counter)) >= 1){
			printf("1");
		}else{
			printf("0");
		}
		counter--;
	}
}

unsigned liesbit(void){
	char zahl[16];
	unsigned int ergebnis;
	int i, len;
	int exp = 0;
	ergebnis = 0;
	
	scanf("%s", zahl);
	
	for(i=strlen(zahl)-1; i>=0; i--){
		if (zahl[i] == '1'){
			ergebnis +=  pow(2,exp);
			exp +=1;
		}else{
			exp+=1;
		}
	}
	printf("%d", ergebnis);
	
	return ergebnis;
}

int main (int argc, char *argv[]){

	//schreibbit(1337);
	liesbit();
	return 0; 
}
