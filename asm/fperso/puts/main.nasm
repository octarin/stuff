section .data

string db "Here's this fucking string !", 0x0
string2 db "Here's this second fucking string !", 0x0

section .text
global _start

%include "puts.nasm"

_start:

push string
call puts
add esp, 4

push string2
call puts
add esp, 4

mov eax, 1
jmp exit

;_________
;___exit__
;_________
exit:
mov ebx, eax
mov eax, 1
int 0x80

