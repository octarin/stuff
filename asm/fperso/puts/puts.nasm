;____________
;__puts______
;____________

puts:
push ebp
mov ebp, esp

push dword [ebp+8]      ;
call strlen             ; récupère la taille de la chaine dans eax
add esp, 4              ;

mov edx, eax
mov eax, 4
mov ebx, 1
mov ecx, dword [ebp+8]
int 0x80

;affiche en plus de la chaine un retour à la ligne
mov dword [esp], 0x0a0d

mov eax, 4
mov ebx, 1
mov ecx, esp
mov edx, 2
int 0x80

pop ebp
ret

;___________
;__strlen___
;___________

strlen:
push ebp
mov ebp, esp
sub esp, 4

mov dword [esp], 0          ;compteur à zéro
mov esi, dword [ebp + 8]    ;pointeur au début de la chaine

jmp le
lh:
inc dword [esp]
inc esi

le:
cmp byte [esi], 0
jnz lh

pop eax                     ;a little trick, to get directly the ret value in eax
pop ebp
ret

