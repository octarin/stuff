all: printreg

printreg: printreg.nasm
	nasm -f elf printreg.nasm
	gcc printreg.o -o printreg

