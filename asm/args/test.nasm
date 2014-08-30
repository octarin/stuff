section .text

extern puts
global main

main:
    push ebp
    mov ebp, esp

    xor ebx, ebx
    .argloop:

        mov eax, dword [ebp + 0xc]
        mov eax, dword [eax + 4 * ebx]

        test eax, eax
        jz .end

        push eax
        call puts
        add esp, 4

        inc ebx
        jmp .argloop

    .end:

    leave
    ret

