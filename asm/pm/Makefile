all: asm c

asm: test.nasm
	nasm -f elf test.nasm
	gcc -o test_asm test.o

c: test.c
	gcc -o test_c test.c

