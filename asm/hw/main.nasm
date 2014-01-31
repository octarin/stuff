section .data

hw db "Hello world!", 0xa, 0

section .text

global _start

start:
mov eax, 4
mov ebx, 1
mov ecx, hw
mov edx, 13
int 0x80

mov eax, 1
xor ebx, ebx
int 0x80

