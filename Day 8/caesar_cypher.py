def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encryptar' else -shift
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("¿Quieres encryptar o decryptar? ").strip().lower()
        shift = int(input("¿Cuántas letras quieres mover? "))
        text = input("Escribe la palabra: ").strip()
        
        resultado = caesar_cipher(text, shift, mode)
        print(f"\nResultado: {resultado}\n")

        repetir = input("¿Quieres usar el programa otra vez? (si/no): ").strip().lower()
        if repetir != "si":
            print("¡Hasta luego!")
            break
        print("\n" + "-"*40 + "\n")

if __name__ == "__main__":
    main()
