import subprocess

def call_nasm_program(expression):
    # Écrire l'expression dans un fichier temporaire pour le programme NASM
    with open('input.txt', 'w') as f:
        f.write(f"{expression}\n")

    # Assembler le programme avec NASM
    subprocess.run(['nasm', '-f', 'elf32', 'calculatrice.asm'], check=True)
    # Lier avec GCC
    subprocess.run(['gcc', '-m32', '-o', 'calculatrice', 'calculatrice.o'], check=True)

    # Appeler le programme compilé
    output = subprocess.run(['./calculatrice'], capture_output=True, text=True)

    return output.stdout.strip()
