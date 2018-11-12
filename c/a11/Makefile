CC = cc
CFLAGS = -g -std=c99 -Wall -pedantic

.PHONY: run clean

all: a11

encrypt: a11
	./a11 encrypt
decrypt: a11
	./a11 decrypt

clean:
	-/bin/rm -f a11
