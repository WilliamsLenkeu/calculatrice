import subprocess


def main():
    print("Calculatrice Simple")
    while True:
        # Demander à l'utilisateur d'entrer une expression
        expression = input("Entrez une expression (ex: 1 + 1) ou 'q' pour quitter: ")

        if expression.lower() == 'q':
            break

        # Analyser l'expression
        try:
            parts = expression.split()
            if len(parts) != 3:
                raise ValueError("Format incorrect. Utilisez : 'nombre opérateur nombre'.")

            num1 = int(parts[0])
            operator = parts[1]
            num2 = int(parts[2])

            # Appeler le code assembleur MIPS avec les valeurs
            result = call_mips_program(num1, operator, num2)
            print(f"Le résultat est: {result}")

        except Exception as e:
            print(f"Erreur: {e}")


def call_mips_program(num1, operator, num2):
    # Écrire les valeurs dans un fichier temporaire pour le programme MIPS
    with open('input.txt', 'w') as f:
        f.write(f"{num1}\n{operator}\n{num2}\n")

    # Exécuter le programme assembleur MIPS
    subprocess.run(['spim', '-file', './calculatrice.asm'], check=True)

    # Lire le résultat du fichier de sortie
    with open('output.txt', 'r') as f:
        result = f.read().strip()

    return result


if __name__ == "__main__":
    main()
