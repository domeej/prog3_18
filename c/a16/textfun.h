#include <stddef.h>
#include <stdlib.h>
#define HSIZE 25


typedef struct listEle{
	struct listEle *next;
	char word[HSIZE];
	char replacement[HSIZE];
} ListEle;


ListEle *wordList;

void addPair(const char *such, const char *ersatz);

void clearList(void);

char *find(const char *s);

int replaceAll(char *s);
