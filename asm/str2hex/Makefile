all: a

a: a.nasm
	nasm -f elf32 -Wall a.nasm
	gcc -s -m32 -o a a.o


