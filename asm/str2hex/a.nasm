section .data

hexasym db "0123456789abcdef"
hexaprefix db "\x"
hexaspace db "20"

section .bss

buf resb 50000

section .text

extern puts
global main

main:
    push ebp
    mov ebp, esp

    mov ebx, 1          ; on initialise le compteur de boucle de manière à ne pas afficher le nom du programmme
    mov esi, buf        ; le pointeur sur la chaine de sortie

    .argloop:

        mov eax, dword [ebp + 0xc]
        mov eax, dword [eax + 4 * ebx]    ; eax contient l'adresse de l'argument courant

        test eax, eax                     
        jz .end                           ; On arrête si argv[ebx] == NULL

        call str2hex                      ; ebx n'est pas modifié, esi pointe sur la fin de la chaine ce qui
                                          ; permet de concaténer les arguments entre eux

        inc ebx
        jmp .argloop

    .end:
    push buf
    call puts                             ; affiche la chaine de sortie

    mov eax, 0
    leave
    ret

; Notre fonction pour afficher les strings en hexadécimal
; eax: adresse de la string
; ebx: si supérieur à un entraine l'ajout d'un séparateur (un espace)
str2hex:
    cmp ebx, 1
    je .carloop

    ; ebx > 1 => on rajoute un espace
    mov edx, dword [hexaprefix]     ;hexaprefix+hexaspace
    mov dword [esi], edx
    add esi, 4

    .carloop:

        xor edx, edx

        mov dl, byte [eax]          ; dl contient le caractère
        test dl, dl
        jz .end

        mov word [esi], '\x'
        add esi, 2                  ; écrit "\x" avant chaque nombre en hexa

        mov ecx, edx

        ; 4 bits de poids fort
        shr dl, 4
        and dl, 0xf
        mov dl, byte [hexasym + edx]
        mov byte [esi], dl
        inc esi

        ; 4 bits de poids faible
        mov dl, cl
        and dl, 0xf
        mov dl, byte [hexasym + edx]
        mov byte [esi], dl
        inc esi

        inc eax                     ; on passe au caractère suivant
        jmp .carloop

    .end:


    mov byte [esi], 0               ; rajout d'un octet nul à la fin du buffer de manière à le rendre affichable par puts

    ret

