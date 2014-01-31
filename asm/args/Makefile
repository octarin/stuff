all: asm s

asm: test.nasm
	nasm -f elf32 test.nasm
	gcc test.o -o test

s: s.c
	gcc s.c -o s
