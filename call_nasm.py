import subprocess

def call_nasm_program(expression):
    # Écrire l'expression dans un fichier temporaire pour le programme NASM
    with open('input.txt', 'w') as f:
        f.write(f"{expression}\n")

    # Exécuter le programme assembleur NASM
    subprocess.run(['nasm', '-f', 'win32', 'calculatrice.asm'], check=True)
    subprocess.run(['gcc', '-o', 'calculatrice', 'calculatrice.obj'], check=True)

    # Appeler le programme compilé
    output = subprocess.run(['calculatrice.exe'], capture_output=True, text=True)

    return output.stdout.strip()
