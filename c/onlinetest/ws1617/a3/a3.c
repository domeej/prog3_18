#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct list{
	char data;
	struct list *next;
}list;

int count(list *lis){
	int i = 0;
	while(lis != NULL){
		lis = lis->next;
		i+=1;
	}
	return i;
}

list *rotate_left(list *lis){
	list *head = lis;
	list *first = lis;
	list *act = lis;
	int anzahl = count(lis);
	
	if(anzahl>=3){
		/* das letzte finden */
		while(act->next != NULL){
			act = act->next;
		}
		/* das letzte zeigt auf das erste */
		act->next = first;
		
		/* head zeigt auf das zweite */
		head = lis->next;
		
		/* das erste zeigt auf NULL */
		first->next = NULL;
		
		return head;
	}
	if(anzahl == 1){
		return lis;
	}
	
	if(anzahl == 2){
		while(act->next != NULL){
			act = act->next;
		} 
		act->next = first;
		first->next = NULL;
		head = act;
		
		return head;
	}
	else
		return NULL;
	
		
	
}

list *rotate_right(list *lis){
	list *head = lis;
	list *act = lis;
	list *first = lis;
	list *prelast;
	list *last;
	int anzahl = count(lis);
	
	if(anzahl>=3){
		/*das vorletzte finden*/
		while(act->next->next != NULL){
			act = act->next;
		}
		prelast = act;
		last = act->next;

		/*das letzte zeit auf das erste */
		last->next = first;
		/*das vorletzte zeigt auf NULL*/
		prelast->next = NULL;

		/*head zeigt auf das letzte*/
		head = last;
		
		return head;
	}
	
	if(anzahl == 1){
		return lis;
	}
	
	if(anzahl == 2){
		while(act->next != NULL){
			act = act->next;
		} 
		act->next = first;
		first->next = NULL;
		head = act;
		
		return head;
	}
	else
		return NULL;

	
}



void printit(list *lis){
	int i = 0;
	while(lis != NULL){
		printf("%c ->", lis->data);
		lis = lis->next;
		i+=1;
	}
	printf(" i:%d \n", i);

}
void delete(list *lis){
	list *temp;
	
	while(lis->next != NULL){
		temp = lis;
		lis= lis->next;
		free(temp);
	}
	free(lis);
}

int main(int argc, char *argv[]){ 
	
	list a;
	list b; 
	list c;
	list *ptr = NULL;
	a.data = 'a';
	b.data = 'b';
	c.data = 'c';
	a.next = &b;
	b.next = &c;
	c.next = NULL;
	printit(&a);
	ptr = rotate_right(&a);
	printit(ptr);
	//delete(a);

	return 0;
}


int main2(int argc, char *argv[]){ 
	
	list *a = malloc(sizeof(list));
	list *b = malloc(sizeof(list)); 
	list *c = malloc(sizeof(list));
	a->data = 'a';
	b->data = 'b';
	c->data = 'c';
	a->next = b;
	b->next = c;
	c->next = NULL;
	printit(a);
	a = rotate_right(a);
	printit(a);
	delete(a);

	return 0;
}
