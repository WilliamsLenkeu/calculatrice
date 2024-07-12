section .data
    input1 db 0
    operator db 0
    input2 db 0
    result db 0
    prompt db "Entrez une expression (ex: 1 + 1): ", 0
    newline db 10, 0

section .bss
    num1 resb 4
    num2 resb 4

section .text
    global _start

_start:
    ; Afficher le prompt
    mov eax, 4
    mov ebx, 1
    mov ecx, prompt
    mov edx, 37 ; longueur du prompt
    int 0x80

    ; Lire le premier nombre
    call read_number
    mov [num1], al

    ; Lire l'opérateur
    call read_operator
    mov [operator], al

    ; Lire le deuxième nombre
    call read_number
    mov [num2], al

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

read_number:
    ; Simplicité, on suppose qu'un seul caractère est lu
    mov eax, 3
    mov ebx, 0
    mov ecx, num1
    mov edx, 1
    int 0x80
    mov al, [num1]
    sub al, '0'  ; Convertir en entier
    ret

read_operator:
    mov eax, 3
    mov ebx, 0
    mov ecx, operator
    mov edx, 1
    int 0x80
    mov al, [operator]
    ret
