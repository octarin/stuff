section .data

strhex db "0123456789abcdef"

section .bss

out_buffer resb 12

section .text

global main
global ntohex

main:
    push ebp
    mov ebp, esp

    mov esi, esp
    mov eax, 0x1337
    call ntohex

    mov eax, 4
    mov ebx, 1
    mov ecx, esi
    mov edx, 9
    int 0x80

    mov esi, esp
    mov eax, 0xdeadbeef
    call ntohex

    mov eax, 4
    mov ebx, 1
    mov ecx, esi
    mov edx, 9
    int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80

    leave
    ret

ntohex:

    mov ecx, 0
    mov edx, eax

    .head:

    mov ebx, edx

    mov eax, 7
    sub eax, ecx
    shl eax, 2
    push ecx
    mov ecx, eax
    shr ebx, cl
    and ebx, 0xf    ;bx contient le chiffre

    mov eax, strhex
    add eax, ebx
    mov bh, byte [eax]  ;bh contient la lettre

    mov byte [esi], bh
    inc esi
    pop ecx
    inc ecx

    cmp ecx, 8
    jl .head

    mov byte [esi], 0xa
    sub esi, ecx

    ret

