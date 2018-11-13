CC = cc
CFLAGS = -g -std=c99 -Wall -pedantic

.PHONY: run clean

all: a13

run: a13
	valgrind --leak-check=full --show-leak-kinds=all ./a13 ene mene mu und aus bist Du

clean:
	-/bin/rm -f a13
