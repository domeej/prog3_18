#include <stdio.h>
#include <ctype.h>
#include <string.h>

#define SIZE 100

void soundex(const char s[], char res[]){
	const char *p = NULL;
	const char *start = NULL;
	char c;
	int i = 0;
	char previous = '#';
	start = s;
	p = s;
	c = toupper(*p);
	res[i]=c;
	i++;
	p++;
	
	while(*p){
		c = toupper(*p);
		
		if(strchr("BFPV", c) != NULL && previous != '1'){
			res[i] = '1';
			previous = '1';
			i++;
		}else if(strchr("CGJKQSXZ", c) != NULL && previous != '2'){
			res[i] = '2';
			previous = '2';
			i++;
		}else if(strchr("DT", c) != NULL && previous != '3'){
			res[i] = '3';
			previous = '3';
			i++;
		}else if(c == 'L' && previous != '4'){
			res[i] = '4';
			previous = '4';
			i++;
		}else if(strchr("MN", c) != NULL && previous != '5'){
			res[i] = '5';
			previous = '5';
			i++;
		}else if(c == 'R' && previous != '6'){
			res[i] = '6';
			previous = '6';
			i++;
		}
		p++;
		if(i == 5){
			break;
		}
	}
	while (i <= 5){
		res[i] = '0';
		i++;
	}
	res[i] = '\0';
	printf("%s\n", res);
}

int main (int argc, char *argv[]){
	char res[SIZE];
	char s[SIZE] = {0};
	
	while(scanf("%s", s) != EOF){
		soundex(s, res);
	}
}
