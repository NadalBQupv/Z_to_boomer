"""Módulo con la lógica de traducción entre jerga Gen Z y español estándar."""

from diccionario import JERGA_GENZ


def traducir_a_boomer(frase: str) -> str:
    """Traduce una frase con términos Gen Z a lenguaje estándar.

    Args:
        frase: Texto de entrada escrito por el usuario.

    Returns:
        La frase con los términos conocidos sustituidos.
    """
    palabras: list[str] = frase.split()
    resultado: list[str] = []

    for palabra in palabras:
        # Signos puntuación:
        nueva_palabra = ""
        symbols_before = ""
        for letter in palabra:
            if letter.isalpha():
                nueva_palabra = nueva_palabra + letter
                symbols_after = ""
            else:
                # Compruebo si el símbolo va antes o después
                if nueva_palabra:
                    # va después
                    symbols_after = symbols_after + letter
                else:
                    symbols_before = symbols_before + letter
        palabra = nueva_palabra


        # Inicio de frase:
        cap = False
        if palabra[0].isupper():
            cap = True
        
        if palabra.lower() in JERGA_GENZ:
            res = JERGA_GENZ[palabra]
            if cap:
                res = res[0].upper() + res[1:]
            resultado.append(symbols_before + res + symbols_after)
        else:
            resultado.append(symbols_before + palabra + symbols_after)

    return " ".join(resultado)


def traducir_a_genz(frase: str) -> str:
    """Traduce una frase estándar a jerga Gen Z.

    Args:
        frase: Texto en español estándar.

    Returns:
        La frase adaptada a jerga juvenil.
    """
    return frase