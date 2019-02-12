#include <stdio.h>


int isPalindrome(char *str){
	char *start = str;
	char *end = str;
	
	while(*end != '\0'){
		end++; 
	}
	end--;
	while(*start == *end || *start == '\0'){
		if (*start == '\0'){
			return 1;
		}
		start++;
		end--;
	}	
	return 0;
}
 


int main (int argc, char *argv[]){
	char str[] = "madame";
	 

	printf("%d",isPalindrome(str));
	
	return 0;
}
