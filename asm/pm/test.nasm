section .data

ch1 db "Trop petit !", 0h
ch2 db "Trop grand !", 0h
ch3 db "Bravo ! Vous avez gagné !", 0h

in1 db "Entrez un nombre : ", 0h
in2 db "%d", 0h

section .text

global main
extern printf
extern puts
extern scanf

main:
push ebp
mov ebp, esp
sub esp, 4

mov dword [esp], 0

lh:

push in1
call printf
add esp, 4

push esp
push in2
call scanf
add esp, 8

cmp dword [esp], 0x2a
jl inferieur
jg superieur

; égal
push ch3
jmp le

inferieur:
push ch1
jmp le

superieur:
push ch2

le:
call puts
add esp, 4
cmp dword [esp], 0x2a
jne lh

;exit

leave
ret

