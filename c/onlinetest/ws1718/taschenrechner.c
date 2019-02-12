#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

typedef struct ele{
	int value;
	struct ele *next;

}StackEle;

enum Operation {OP_ADD, OP_MUL, OP_DUP, OP_DROP };

StackEle* push(StackEle *stack, int value){
	StackEle *p = stack;
	StackEle *new = NULL;
	
	if (p == NULL){
		p = malloc(sizeof(StackEle));
		p->next = NULL;
		p->value = value;
		return p;
	}
	else{
		new = malloc(sizeof(StackEle));
		new->next = p;
		new->value  = value;
		return new;
	}
} 

void deleteStack(StackEle *stack){
	StackEle *temp = stack;
	while(stack != NULL){
		temp = stack;
		stack = stack->next;
		free(temp);
	}
}

void printStack(StackEle *stack){
	
	if (stack == NULL){
		printf("whoot:%d", stack->value);
		printf("Stack leer!\n");
	}
	
	if (stack != NULL){
		while(stack != NULL){
			printf("%d->",stack->value);
			stack = stack->next;
		}
		printf("\n");
	}
}

void operation(StackEle *stack, enum Operation op){
	if((stack != NULL) || (stack->next != NULL)){
		StackEle *first = stack;
		StackEle *second = stack->next;
		int newValue = 0;
	
		if (op == OP_ADD){
			newValue = first->value + second->value;
			first->value = newValue;
			first->next = first->next->next;
			free(second);
			
		}
		if (op == OP_MUL){
			newValue = first->value * second->value;
			first->value = newValue;
			first->next = first->next->next;
			free(second);
		}
		
		if (op == OP_DUP){
			StackEle *new = malloc(sizeof(StackEle));
			new->value = first->value;
			new->next = first->next;
			first->next = new; 
		}
	}
	if (op == OP_DROP){
		StackEle *temp;
		
		if(stack == NULL){
		
		} 
		
		else if (stack->next == NULL){
			printf("nur ein element\n");
			free(stack);
			
		}
		else if (stack->next->next != NULL){
			stack->value = stack->next->value;
			temp = stack->next;
			stack->next = stack->next->next;
			free(temp);
		}else{
			stack->value = stack->next->value;
			temp = stack->next;
			stack->next = stack->next->next;
			free(temp);
		}
		
	}
}


int main (int argc, char *argv[]){
	/*StackEle stack;
	StackEle v1;
	StackEle v2;
	StackEle v3;
	StackEle v4;
	v1.value = 1;
	v2.value = 5;
	v3.value = 3;
	v4.value = 7;
	v1.next = &v2;
	v2.next = &v3;
	v3.next = &v4;
	v4.next = NULL;
	stack = v1;
	*/
	StackEle *test = NULL;
	test = push(test, 7);
	test = push(test, 3);
	test = push(test, 5);
	test = push(test, 1);
	
	/*
	printStack(&stack);
	operation(&stack, OP_ADD);
	printStack(&stack);
	*/
	printStack(test);
	operation(test, OP_ADD);
	printStack(test);
	operation(test, OP_MUL);
	printStack(test);
	operation(test, OP_DUP);
	printStack(test);
	operation(test, OP_DROP);
	printStack(test);
	operation(test, OP_DROP);
	printStack(test);
	operation(test, OP_DROP);
	printStack(test);
	operation(test, OP_DROP);
	printStack(test);
	operation(test, OP_DROP);
	printStack(test);
	operation(test, OP_DROP);
	printStack(test);

	
	
	deleteStack(test);

	return 0;
}
