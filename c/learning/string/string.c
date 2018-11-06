#include <stdio.h>
#include <string.h>
#define SIZE 70

FILE *fp = NULL;
void classic(FILE *fp);
void pointer(FILE *fp);
void standartFor(FILE *fp);
int searchWord(FILE *fp, char *word);

int main (int argc, char *argv[]){
	char word[SIZE] = "Sir";
	fp = fopen("example.txt", "r");
	
	if(fp == NULL){
		printf("Datei konnte nicht gefunden werden!/n");	
	}
	/*standartFor(fp);*/
	
	printf("Anzahl an %s: %d\n", word, searchWord(fp, word));
	
	fclose(fp);
	
	return 0;
}

void classic(FILE *fp){
	char line[SIZE];
	
	while(fgets(line, SIZE, fp) != NULL){
		printf("%s", line);
	} 
}

void pointer(FILE *fp){
	char line[SIZE];
	char *act;
	
	while(fgets(line, SIZE, fp) != NULL){
		act  = line;
		while(*act){
			printf("%c", *act);
			act++;
		}
	}
}

void standartFor(FILE *fp){
	char line[SIZE];
	int i;
	while(fgets(line, SIZE, fp) != NULL){
		for(i = 0; i<strlen(line); i++){
			printf("%c", line[i]);
		}
	} 
}

/* nach wort im text suchen */
int searchWord(FILE *fp, char *word){
	char line[SIZE];
	char *part;
	char *found;
	int counter = 0;
	int len = 0;
	
	while(fgets(line, SIZE, fp) != NULL){
		part = line;
		while(*part){
			found = strcasestr(part,word);
			len = strlen(word);
			
			if (found != NULL){
				/*printf("%s\n",  found);*/
				part = found+len;
				counter +=1;
			}
			part++;
		}
		found = strcasestr(line, word);
	}
	return counter;
}
