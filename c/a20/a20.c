#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "textfun.h"
#define SIZE 200

char* censorWord(char *s, char *word){
	char *act;
	char *found;
	int wordLen = strlen(word), i=1, pos=1;
	/*printf("loesche '%s' aus dem Text ...\n", word);*/
	act = s;
	
	while(pos < strlen(s)){
		found = strcasestr(act, word);
		/* gehe ein Zeichen weiter */
		if(found != NULL){
			found+=1;
			pos+=1;
			while(i<wordLen){
				*found = '*';
				found++;
				i++;
				pos++;
			}
			i=1;
			act = found;
		}else{
			break;
		}
	}
	return s;
}

void makeSave(char *s, int argc, char *argv[]){
	char result[SIZE] = {0};
	int i = 1;
	
	while(i<argc){
		strcpy(result ,censorWord(s, argv[i]));
		i++;
	}
	printf("%s", result);
}

int main (int argc, char *argv[]){
	int i;
	char s[SIZE];
	char *found = NULL, *key = NULL, *value = NULL;
	for(i = 1; i < argc; i++){
		found = strchr(argv[i], '=');
		value = found+1;
		*found = 0;
		key = argv[i];
		
		addPair(key, value);		
	}
	printPairs();
	
	while(fgets(s, SIZE, stdin) != NULL){
		replaceAll(s);
	}
	serializeList();
}

