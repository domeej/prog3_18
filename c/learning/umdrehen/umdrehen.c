#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void umdrehen(char *str){
	char *copy = NULL;
	char *start = str;
	char *end = NULL;
	
	copy = malloc(sizeof(char) * strlen(str)+1);
	strcpy(copy, str);
	end = copy;

	while(*end != '\0'){
		end++;
	}
	end--;
	
	while(*start != '\0'){
		strncpy(start, end, 1);	
		start++;
		end--;
	}
	free(copy);
	printf("%s", str);
}
 


int main (int argc, char *argv[]){
	char str[] = "Hallo Welt!";
	umdrehen(str);
	return 0;
}
