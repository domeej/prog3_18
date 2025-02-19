#include <stdlib.h>
#include <string.h>
#include "textfun.h"
#include <stdio.h>
#define SIZE 25
#define FILENAME "glogomir.txt"


ListEle *wordList = NULL;

void addPair(const char *such, const char *ersatz){
	ListEle *act = wordList;

	if(wordList == NULL){
		wordList = malloc(sizeof(ListEle));
		wordList->next = NULL;
		strcpy(wordList->word, such);
		strcpy(wordList->replacement, ersatz);
		act = wordList;
		
	}else{
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
}

void printPairs(){
	ListEle *p;
	p = wordList;
	if(p==NULL){
		printf("keine Paare vorhanden");
	}
	while(p!=NULL){
		printf("%s->", p->word);
		if(p->next  == NULL){
			printf("NULL");
		}
		p=p->next;
		
	}
	printf("\n");
	
}

void clearList(void){
	ListEle *toDelete = NULL;
	
	while(wordList != NULL){
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
	char *found, *p, *substr = NULL;
	int counter = 0;
	char safe [100]; 
	
	substr = s;
	
	while(act != NULL){
		while((found = strstr(substr, act->word)) != NULL){
			 /* prüfen ob such- oder ersetz-wort länger ist und substr entsprechend platzieren*/
			 if(strlen(act->replacement) >= strlen(act->word)){
				/*ersetz wort größer*/
				strcpy(safe, found+strlen(act->word));
				strcpy(found, act->replacement);
				strcat(found, safe);
				
			 }else{
				/* ersetz wort kleiner */
				strcpy(found, act->replacement);
				p = found;
				p = p+strlen(act->replacement)+3;
				strcpy(safe, p);
				strcat(found, safe);
			 }
			found = NULL;
			counter++;
			substr = substr+strlen(act->replacement);
		}
		act = act->next;
	}
	printf("%s\n", s);
	return counter;
}

void serializeList(){
	FILE *fp = fopen(FILENAME, "w");
	ListEle *p;
	p = wordList;
	printf("serialisiere...\n");

	while(p!=NULL){
		fputs(p->word, fp);
		fputs(":", fp);
		fputs(p->replacement, fp);
		fputs("\n", fp);
		p=p->next;
		
	}
	fclose(fp);
}

void deserializeList(){
	FILE *fp = fopen(FILENAME, "r");
	char word[255];
	char *p;

	char replacement[255]; 
	printf("BAMdeserialize...\n");

	
	while(fgets(word, 255, fp)!= NULL){
		p = strchr(word, ':');
		*p = 0;
		p+=1;
		strncpy(replacement, p, strlen(p)-1);
		addPair(word, replacement);
	} 
	
	
	fclose(fp);
	
}
