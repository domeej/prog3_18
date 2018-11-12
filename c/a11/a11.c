#include <stdio.h>
#include <string.h>

#define SIZE 100

void encrypt(char *text, char *a, char *b){
	char *found = NULL;
	char result[SIZE] ={0};
	int i, index,len = strlen(text);
	
	for(i = 0; i < len-1; i++){
		found = strchr(a, text[i]);
		
		if (found != NULL){
			index = found - a;
			result[i] = b[index];
		}else{
			result[i] = text[i];
		}
	}
	result[i+1] = '\0';
	printf("\n%s", result);
}
void decrypt(char *text, char *a, char *b){
	encrypt(text,b,a);
}

int main (int argc, char *argv[]){
	char a[] = "abcdefghijklmnopqrstuvwxyz";
	char b[] = "wgsnqcdvmeyluzoabhrjfkxipt";
	char text[SIZE];
	int i =0;
	while((text[i] = getchar()) != EOF){
		i++;
	}

	if(strcmp(argv[1], "decrypt")==0){
		decrypt(text,a,b);
	}else if(strcmp(argv[1], "encrypt")==0){
		encrypt(text,a,b);
	}
}
