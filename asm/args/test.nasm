section .text

extern puts
global main

main:
push ebp
mov ebp, esp
sub esp, 4

mov eax, dword [ebp+8]
mov dword [esp], eax ; on stocke le nombre d'arguments

xor ebx, ebx ; on initialise le compteur de boucle

lh:

mov eax, dword [ebp + 0xc]
mov edx, 4
imul edx, ebx
add eax, edx
mov eax, dword [eax]

push eax
call puts
add esp, 4

inc ebx
cmp ebx, dword [esp]
jl lh

mov eax, 0

leave
ret

