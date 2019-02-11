#include <stdio.h>
#include <string.h>
 
/*
 * searchWords splitten bei Leerzeichen
 * replWords splitten bei Leerzeichen
 * -> beide als Array aus Pointern auf Strings speichern
 * 	arr[0] --> char *p --> "string"
 * 
 * 
 * */
 
int stringsToArray(char *str, char *arr[]) {
	char *splitter = " ";
	char *token;
	int i = 0;

	/* array bauen */
	token = strtok(str, splitter);
	while(token != NULL){
		arr[i] = token;
		token = strtok(NULL, splitter);
		i++;
	}
	return i;
}

void printArray(char *arr[], int size){
    int i = 0;
    while(i<size){
		printf("%s,", arr[i]);
		i++;
    }
	printf("\n");
}
 
void replaceWords(char *s, char *search[], char *replace[], int size){
	char *p = s;
	int i = 0;
	char copy[100];
	
	
	while(i<size){
		p = strstr(s, search[i]);
		printf("p:%s\n", p);
		while(strstr(p, search[i])){
			p = strstr(p, search[i]);
			printf("p:%s\n", p);
			strcpy(copy, p + strlen(search[i]));
			strcpy(p, replace[i]);
			p += strlen(replace[i]);
			strcpy(p, copy);
		}
		i+= 1;
	}
	printf("%s\n", s);

	
}
 
int main(void) {
    char s[] = "Ein Vogel flog durch den Wald";
    char ts[] = "Ein Vogel flog durch den Wald";
    char searchWords[] = "Vogel flog Wald";
    char replWords[] = "Hund lief Garten";
	char *seArr[100];
	char *reArr[100];
	
	int anzahl = 0;
	int arrSize, i;
	arrSize = stringsToArray(searchWords, seArr);
    stringsToArray(replWords, reArr);
    
    printArray(seArr, arrSize);
    printArray(reArr, arrSize);
    
    replaceWords(ts, seArr, reArr, arrSize);
    
    return 0;
}
