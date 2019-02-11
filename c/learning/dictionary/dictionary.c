#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct ele {
	char *key;
	int value;
	struct ele *next;
}ele;

ele* addKeyValue(ele *dict, char *key, int value);
ele* delete(ele *dict, char *key);
int getValueAt(ele *dict, char *key);

ele* addValueAt(ele *dict, char *key, int value){
	ele *act = dict;
	
	while(0 != strcmp(act->key, key)){
		act = act->next;
	}
	act->value += value;
	return dict;
}

int getValueAt(ele *dict, char *key){
	ele *act = dict;
	ele *test = dict;
	int exists = 0;
	while(test->next != NULL){
		if(0 == strcmp(test->key, key)){
			exists = 1;
		}
		test = test->next;
	}
	if (exists){	
		while(0 != strcmp(act->key, key)){
			act = act->next;
		}
		return act->value;
	}
	return -1;
}


ele* delete(ele *dict, char *key){
	ele *act = dict;
	ele *pre = NULL;
	ele *next = NULL;
	
	if(0 == strcmp(act->key, key)){
		dict = act->next;
		free(act);
		return dict;
	}
	
	while(0 != strcmp(act->next->key, key)){
		act = act->next;
	}
	pre = act;
	next = act->next->next;
	act = act->next;
	pre->next = next;
	free(act);
	return dict;
}

void printDict(ele *dict){
	ele *act = dict;

	while(act){
		printf("%s:%d->", act->key, act->value);
		act = act->next;
	}	
	printf("\n");
}

ele* addKeyValue(ele *dict, char *key, int value){
	ele *p = dict;
	
	if(dict == NULL){
		dict = malloc(sizeof(ele));
		dict->key  = key;
		dict->value = value;
		dict->next = NULL;
		return dict;
	}
	else{
		while(p->next != NULL){
			p = p->next;
		}
		ele *new = malloc(sizeof(ele));
		new->value  = value;
		new->key= key;
		new->next = NULL;	
		p->next = new;
	}
	return dict;
}

void deleteDict(ele *dict){
	ele * temp = NULL;
	
	while(dict->next != NULL){
		temp = dict;
		dict= dict->next;
		free(temp);
	}
	free(dict);
}

ele *updateValue(ele *dict){
	return NULL;

}

int main (int argc, char *argv[]){
	char *haus = "haus";
	char *peter = "peter";
	char *ot = "ot";
	char *sommer = "sommer";
	char *kaffee = "kaffee";
	
	ele *dict = NULL;
	dict = addKeyValue(dict, haus, 1);
	dict = addKeyValue(dict, peter, 2);
	dict = addKeyValue(dict, ot, 2);
	dict = addKeyValue(dict, sommer, 1337);
	dict = addKeyValue(dict, kaffee, 99);
	printDict(dict);
	
	dict = delete(dict, peter);
	printDict(dict);
	dict = addValueAt(dict, kaffee, 70);
	printf("%d", getValueAt(dict, "xx"));
	printDict(dict);
	deleteDict(dict);
	return 0;
}
