#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

#define ALPHABETSIZE 26

typedef struct ele{
	char codezeichen;
	int anzahl;
}Ele;

int comparefunc(const void *a, const void *b){
	int A = ((struct ele*)a)->anzahl;
	int B = ((struct ele*)b)->anzahl;
	
	if (A == B){
		return ((struct ele*)a)->codezeichen - ((struct ele*)b)->codezeichen;
	}
	return ((struct ele*)b)->anzahl - ((struct ele*)a)->anzahl ;
}

void printOccuranceList(Ele list[]){
	int i;
	for(i = 0; i < ALPHABETSIZE; i++){
		printf("%c:%d\n", list[i].codezeichen, list[i].anzahl); 
	
	}

}

void decrypt(FILE *fp, Ele list[]){
	char c, alphabetEncrypted[ALPHABETSIZE] = "eniastruhdlcmogkwbzfvpjxyq";
	int i;
	rewind(fp);
	printOccuranceList(list);
	int found;
	while((c = fgetc(fp)) != EOF){
		//putchar(c);
		found = 0;
		
		for(i = 0; i < ALPHABETSIZE; i++){
			if(toupper(c) == list[i].codezeichen){
				putchar(alphabetEncrypted[i]);
				found = 1;
				break;
			}
		}
		if(!found){
			putchar(c);
		}	
	}
	fclose(fp);
}

void createOccuranceList(FILE *fp){
	Ele list[ALPHABETSIZE];
	int i, counter = 0;
	char c;
	char alphabet[ALPHABETSIZE] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	
	for(i = 0; i < ALPHABETSIZE; i++){
		/* jedes char in File lesen */
		while((c = fgetc(fp)) != EOF){
			c = toupper(c);	
			
			if(c == alphabet[i]){
				counter++;
			}
		}
		list[i].codezeichen = alphabet[i];
		list[i].anzahl = counter;
		
		counter = 0;
		rewind(fp);
	}
	
	qsort(list, ALPHABETSIZE, sizeof(Ele), comparefunc);
	/*printOccuranceList(list);*/
	decrypt(fp, list);
}



int main(int argc, char *argv[]){
	
	if(argc > 1){
		createOccuranceList(fopen(argv[1], "r"));
	}
	else{
		printf("NOOB! kein Dateiname angegeben. Programm beendet.\n");
	}
	
}



