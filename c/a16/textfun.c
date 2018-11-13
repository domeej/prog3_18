#include <stdlib.h>
#include <string.h>
#include "textfun.h"
#define SIZE 25


void addPair(const char *such, const char *ersatz){
	ListEle *act = wordList;
	ListEle *new = malloc(sizeof(ListEle));
	
	new->next = NULL;
	strcpy(new->word, such);
	strcpy(new->replacement, ersatz);
	
	/* ans Ende der Liste laufen*/
	while(act->next != NULL){
		act = act->next;
	}
	act->next = new;
}

void clearList(void){
	ListEle *toDelete = NULL;
	
	while(wordList->next != NULL){
		toDelete = wordList;
		wordList = wordList->next;
		free(toDelete);
	}
	free(wordList);
}


char* find(const char *s){
	ListEle *act = wordList;
	char *found;
	
	while(act != NULL){
		/* vorkommen gefunden */
		if ((found = strstr(s, act->word)) != NULL){
			return found;
		}
		act = act->next;
	}
	return NULL;
}

int replaceAll(char *s){
	ListEle *act = wordList;
	char *found, *subs = NULL;
	int counter = 0;
	subs = s;
	while((found = strstr(s, act->word)) != NULL){
		/* ein wort gefunden, muss ersetzt werden, was bei unterschiedlicher länge??
		 * TODO
		 * */
		found = NULL;
		counter++;
	}
	return -1;
}


int main(void){

	return 0;
}
