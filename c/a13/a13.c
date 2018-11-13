#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SIZE 25

struct node{
	struct node *next;
	char name [SIZE];
};

void printRing(struct node *head){
	struct node *act;
	act = head;
	do{
		printf("%s-->", act->name);
		act = act->next;
	}while(act != head);
	printf("%s\n", act->name);
}

void sortOut(struct node *head, int number){
	/* number = 7 */
	int i = 1;
	struct node *act;
	struct node *toDelete;
	int freeCounter = 0;
	
	act = head;
	
	while(head->next != head){
		/* vorgänger von zu löschendem knoten finden */
		while(i != number-1){
			act = act->next;
			i++;
		}
		i = 1;
		/* gefundenen knoten löschen */
		printf("zu loeschen:%s ", act->next->name);
		
		/* wenn zu loeschendes der head ist */
		if(act->next == head){
			head = act->next->next;
		}
		toDelete = act->next;
		act->next = act->next->next;
		free(toDelete);
		freeCounter +=1;
		act = head;
		printRing(head);
	}
	printf("%s muss spülen!\n", head->next->name);
	free(head);
	freeCounter +=1;
	printf("freeCounter: %d\n", freeCounter);
}

int main (int argc, char *argv[]){
	char name[25] = {0};
	struct node *head = NULL;
	struct node *act = NULL;
	struct node *new = NULL;
	int c = 0;

	while(scanf("%s", name) != EOF){
		if(head == NULL){
			head = malloc(sizeof(struct node));
			head->next = head;
			act = head;
			strcpy(head->name, name);
			c +=1;
		}else{
			/* durch ring laufen bis act.next == head */
			new = malloc(sizeof(struct node));
			strcpy(new->name, name);
			act->next = new;
			new->next = head;
			act = new;
			c +=1;
		}
	}
	printf("mallocs:%d\n", c);
	printRing(head);
	sortOut(head, argc-1);
	return 0;
}
