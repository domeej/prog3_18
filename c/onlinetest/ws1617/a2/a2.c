#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int determineLength(const char *s, const char *a[]){
	int i, newlen;
	char dollar[2];
	i = 0;
	newlen = 0;
	dollar[0] = '$';
	newlen = strlen(s);
	
	while(i<=9){		
		dollar[1] = i + '0';
		
		if (strstr(s, dollar)){
			newlen += strlen(a[i]) - 2;
		}
		i+=1;
	}
	return newlen;
}


char *format(const char *s, const char *a[]){
	int newlen = determineLength(s, a);
	char *newS = malloc(sizeof(char) * newlen);
	char *p, *n;
	int i;
	char dollar[2];
	i = 0;
	dollar[0] = '$';
	
	strcpy(newS, s);
	
	while(i<=9){
		dollar[1] = i + '0';
		p = strstr(s, dollar);
		n = strstr(newS, dollar);
		/* wenn stelle gefunden */
		if (p != NULL){
			n = strcpy(n, a[i]);
			p += 2; 
			strcat(n+ strlen(a[i]), p);
			
			while(strstr(n, dollar)){
				p = strstr(p, dollar);
				n = strstr(newS, dollar);
				n = strcpy(n, a[i]);
				p += 2; 
				strcat(n+ strlen(a[i]), p);
			}
		}
		i+=1;
	}
	
	printf("%s\n", newS);
	free(newS);
	return 0;
}


int main(int argc, char *argv[]){ 
	const char *arr [] = {"a", "bums", "c"};
	const char *arr3 [] = {"a", "b", "c"};
	const char *arr2 [] = {"st"};

	format("$0 und $2.", arr); 
	format("$0$0$0ottern", arr2); 
	format("$17", arr3); 

	return 0;
}
