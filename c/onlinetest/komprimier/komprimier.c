#include <string.h>
#include <stdlib.h>
#include <stdio.h>


void komprimier(char *str){
	char *p = str;
	char *next = str;
	int zaehler = 0;
	char number[100] = {0};
	char *copy = malloc(sizeof(char) *100);
	char *cp;
	cp = copy;

	while(*p != '\0'){
		while(*next == *p){
			zaehler+=1;
			next++;
		}
		if(zaehler > 1){
			sprintf(number, "%d", zaehler);
			strncpy(cp, number, strlen(number));
			cp+= strlen(number);
			strncpy(cp, p, 1); /* ginge auch mit strcpy nur immer '\0' ganz am ende '\0' nicht vergessen! */
			p = next;
			zaehler = 0;
			cp++;
		}else{
			strncpy(cp, p, 1);
			p++;
			cp++;
			zaehler = 0;
		}
	*cp = '\0';
	}
	printf("%s\n", copy);
	free(copy);
}

void komprimierShort(char *str){



}

int main (int argc, char *argv[]){
	char str[] = "abbbccddddefggg";
	komprimier(str);
	return 0;
}
