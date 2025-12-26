import string

def check_length(password):
    length = len(password)

    if length < 8:
        return 0, "Longitud insuficiente (menos de 8 caracteres)"
    elif length < 12:
        return 10, "Longitud aceptable"
    else:
        return 20, "Buena longitud"

def check_case(password):
    has_upper = False
    has_lower = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True

    if has_upper and has_lower:
        return 15, "Contiene mayúsculas y minúsculas"
    elif has_upper or has_lower:
        return 5, "Solo un tipo de letra"
    else:
        return 0, "No contiene letras"

def check_numbers(password):
    for char in password:
        if char.isdigit():
            return 10, "Contiene números"
    return 0, "No contiene números"

def check_special_characters(password):
    special_chars = "!@#$%^&*()-_=+[]{};:,.<>?/"

    for char in password:
        if char in special_chars:
            return 20, "Contiene caracteres especiales"
    return 0, "No contiene caracteres especiales"

def get_security_level(score):
    if score <= 20:
        return "🔴 Contraseña insegura"
    elif score <= 35:
        return "🟠 Contraseña débil"
    elif score <= 50:
        return "🟡 Contraseña aceptable"
    else:
        return "🟢 Contraseña fuerte"

def main():
    password = input("Ingresa una contraseña para evaluar: ")

    total_score = 0

    print("\nResultados de la evaluación:\n")

    score, message = check_length(password)
    total_score += score
    print(f"- Longitud: {message}")

    score, message = check_case(password)
    total_score += score
    print(f"- Letras: {message}")

    score, message = check_numbers(password)
    total_score += score
    print(f"- Números: {message}")

    score, message = check_special_characters(password)
    total_score += score
    print(f"- Caracteres especiales: {message}")

    level = get_security_level(total_score)

    print("\nResultado final:")
    print(f"Puntuación total: {total_score}/65")
    print(f"Nivel de seguridad: {level}")

if __name__ == "__main__":
    main()
