all: hw

hw: main.nasm
	nasm -f elf main.nasm -o hw.o
#	gcc hw.o -o hw
	ld hw.o -o hw -s 

