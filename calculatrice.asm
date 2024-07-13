section .data
    prompt db "Entrez une expression (ex: 1 + 1): ", 0
    newline db 10, 0

section .bss
    expr resb 32
    num1 resb 4
    num2 resb 4
    result resb 4
    operator resb 1

section .text
    global _start

_start:
    ; Afficher le prompt (peut être omis si appelé par Python)
    ; mov eax, 4
    ; mov ebx, 1
    ; mov ecx, prompt
    ; mov edx, 37 ; longueur du prompt
    ; int 0x80

    ; Lire l'expression
    mov eax, 3
    mov ebx, 0
    mov ecx, expr
    mov edx, 32
    int 0x80

    ; Parser l'expression
    call parse_expression

    ; Effectuer l'opération
    mov al, [num1]
    mov bl, [operator]
    mov cl, [num2]

    cmp bl, '+'
    je add_op
    cmp bl, '-'
    je sub_op
    cmp bl, '*'
    je mul_op

add_op:
    add al, cl
    jmp store_result

sub_op:
    sub al, cl
    jmp store_result

mul_op:
    mul cl

store_result:
    mov [result], al

    ; Afficher le résultat
    mov eax, 4
    mov ebx, 1
    mov ecx, result
    mov edx, 1
    int 0x80

    ; Nouvelle ligne
    mov eax, 4
    mov ebx, 1
    mov ecx, newline
    mov edx, 1
    int 0x80

    ; Terminer le programme
    mov eax, 1
    xor ebx, ebx
    int 0x80

parse_expression:
    ; Lire le premier nombre
    mov esi, expr
    call read_number
    mov [num1], al

    ; Lire l'opérateur
    inc esi
    call read_operator
    mov [operator], al

    ; Lire le deuxième nombre
    inc esi
    call read_number
    mov [num2], al
    ret

read_number:
    mov al, [esi]
    sub al, '0'  ; Convertir en entier
    ret

read_operator:
    mov al, [esi]
    ret
