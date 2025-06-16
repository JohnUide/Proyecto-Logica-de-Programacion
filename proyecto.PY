import random

def juego_ahorcado():
    # Lista de palabras secretas
    palabras = ["PYTHON", "PROGRAMACION", "AHORCADO", "COMPUTADORA", "ALGORITMO"]
    palabra_secreta = random.choice(palabras).upper()
    letras_adivinadas = ["_"] * len(palabra_secreta)
    letras_incorrectas = []
    intentos_maximos = 6
    intentos = 0

    print("¡Bienvenido al juego del ahorcado!")
    print(f"Palabra a adivinar: {' '.join(letras_adivinadas)}\n")

    while True:
        # Mostrar estado actual
        print(f"Letras incorrectas: {' '.join(letras_incorrectas)}")
        print(f"Intentos restantes: {intentos_maximos - intentos}")
        
        # Pedir letra al usuario
        letra = input("Ingresa una letra: ").upper()
        
        # Validar entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Error: Ingresa una sola letra válida.\n")
            continue
        
        # Verificar si la letra está en la palabra
        if letra in palabra_secreta:
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    letras_adivinadas[i] = letra
            print(f"\n¡Correcto! {' '.join(letras_adivinadas)}\n")
        else:
            letras_incorrectas.append(letra)
            intentos += 1
            print(f"\nLetra incorrecta. Te quedan {intentos_maximos - intentos} intentos.\n")
        
        # Condiciones de fin del juego
        if "_" not in letras_adivinadas:
            print(f"¡Felicidades! Adivinaste la palabra: {palabra_secreta}")
            break
        if intentos >= intentos_maximos:
            print(f"¡Perdiste! La palabra era: {palabra_secreta}")
            break

# Iniciar el juego
if __name__ == "__main__":
    juego_ahorcado()