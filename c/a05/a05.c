#include <stdio.h>
#include <ctype.h>

void rot13();

int main (int argc, char *argv[]){
	
	rot13();
	
}


void rot13(){
	int c; // char ergibt hier ein Fehler char c
	
	while((c = getchar()) != EOF){
		// A = '65' Z = '90'
		if (isalpha(c)){
			if (islower(c)){
				c = c+13;
				if (c > 'z'){
					c = (c % 'z') + 96;
					
				}
			}
			if (isupper(c)){
				c = c+13;
				if (c > 'Z'){
					c = (c % 'Z') + 64;
					
				}	
			}
			printf("%c", c);
		}
		else{
			printf("%c", c);
		}
	}
}
